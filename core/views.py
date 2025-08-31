# core/views.py

from django.shortcuts import render
# Importe os "produtos" que queremos buscar do nosso depósito (site_setup)
from site_setup.models import HeaderLogo, HeroImage, PartnerLogo

def home(request):
    # O gerente vai ao depósito e pega tudo de cada prateleira
    header_logos = HeaderLogo.objects.all()
    hero_images = HeroImage.objects.all()
    partner_logos = PartnerLogo.objects.all()

    # Agora, ele cria um "pacote de entrega" (o contexto) com tudo que pegou
    context = {
        'header_logos': header_logos,
        'hero_images': hero_images,
        'partner_logos': partner_logos,
    }
    
    # Finalmente, ele entrega o pacote para a vitrine (o template)
    return render(request, 'home.html', context)

def quero_vender(request):
    # Por enquanto, ela só precisa renderizar o novo template
    return render(request, 'quero_vender.html')