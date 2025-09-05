from django.db import models
from django.utils.text import slugify

class GraficoECharts(models.Model):
    titulo = models.CharField(
        max_length=200, 
        unique=True, 
        help_text="Título interno para identificar o gráfico no painel de administração."
    )
    chave = models.SlugField(
        max_length=220, 
        unique=True, 
        blank=True, 
        help_text="Chave de texto única gerada automaticamente para usar no texto (ex: [grafico:minha-chave])."
    )
    codigo_js = models.TextField(
        verbose_name="Código JavaScript do Gráfico",
        help_text="Cole aqui o código JavaScript da 'option' do seu gráfico ECharts."
    )

    def save(self, *args, **kwargs):
        if not self.chave:
            self.chave = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Gráfico"
        verbose_name_plural = "Gráficos"

class ConteudoInteligencia(models.Model):
    CATEGORIA_CHOICES = [
        ('DADOS_ESTRUTURAIS', 'Dados Estruturais'),
        ('ANALISES_E_ARTIGOS', 'Análises e Artigos'),
    ]
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, verbose_name="Categoria")
    titulo_card = models.CharField(max_length=100, verbose_name="Título do Card", help_text="Título que aparece na listagem de cards.")
    imagem_card = models.ImageField(upload_to='intelligence/cards/', verbose_name="Imagem do Card", help_text="Imagem de capa que aparece na listagem.")
    titulo_interno = models.CharField(max_length=200, verbose_name="Título do Conteúdo", help_text="Título principal exibido dentro da página do conteúdo.")
    subtitulo = models.CharField(max_length=300, blank=True, null=True, verbose_name="Subtítulo", help_text="Texto curto que aparece abaixo do título principal.")
    corpo_texto = models.TextField(verbose_name="Corpo do Conteúdo", help_text="O conteúdo principal do artigo. Use [grafico:sua-chave] para inserir um gráfico.")

    def __str__(self):
        return self.titulo_card

    class Meta:
        verbose_name = "Conteúdo"
        verbose_name_plural = "Conteúdos"
        ordering = ['categoria', 'titulo_card']
        
class GlossarioTermo(models.Model):
    termo = models.CharField(max_length=100, unique=True, verbose_name="Termo")
    explicacao = models.TextField(verbose_name="Explicação", help_text="Use as ferramentas de formatação para criar uma explicação clara.")

    def __str__(self):
        return self.termo

    class Meta:
        verbose_name = "Termo do Glossário"
        verbose_name_plural = "3. Glossário de Termos"
        ordering = ['termo']