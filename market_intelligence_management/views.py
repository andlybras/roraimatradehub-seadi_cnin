import re
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.template.loader import render_to_string
from .models import ConteudoInteligencia, GraficoECharts

def inteligencia_mercado_view(request):
    categorias_tuplas = ConteudoInteligencia.CATEGORIA_CHOICES
    categorias = {chave: valor for chave, valor in categorias_tuplas}
    context = {
        'categorias': categorias
    }
    return render(request, 'market_intelligence/inteligencia_mercado.html', context)

def listar_cards_por_categoria_view(request, categoria):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        raise Http404

    cards = ConteudoInteligencia.objects.filter(categoria=categoria).order_by('titulo_card')
    html = render_to_string('market_intelligence/partials/lista_cards.html', {'cards': cards})
    
    return JsonResponse({'html': html})

def detalhar_card_view(request, card_id):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        raise Http404

    try:
        card = ConteudoInteligencia.objects.get(id=card_id)
        
        def substituir_grafico(match):
            chave = match.group(1)
            try:
                grafico = GraficoECharts.objects.get(chave=chave)
                container_id = f"grafico-container-{grafico.chave}"
                script_grafico = f"""
                    <div id='{container_id}' style='width: 100%; height: 400px;'></div>
                    <script type='text/javascript'>
                        var chartDom = document.getElementById('{container_id}');
                        var myChart = echarts.init(chartDom);
                        var option = {grafico.codigo_js};
                        myChart.setOption(option);
                    </script>
                """
                return script_grafico
            except GraficoECharts.DoesNotExist:
                return f"<p style='color: red;'>[Gráfico com a chave '{chave}' não encontrado.]</p>"

        corpo_processado = re.sub(r'\[grafico:([\w-]+)\]', substituir_grafico, card.corpo_texto)

        context = {
            'card': card,
            'corpo_processado': corpo_processado
        }
        
        html = render_to_string('market_intelligence/partials/detalhe_card.html', context)
        return JsonResponse({'html': html})

    except ConteudoInteligencia.DoesNotExist:
        return JsonResponse({'error': 'Card não encontrado.'}, status=404)