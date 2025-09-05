from django.contrib import admin
from .models import GraficoECharts, ConteudoInteligencia
from tinymce.widgets import TinyMCE
from django.db import models

@admin.register(GraficoECharts)
class GraficoEChartsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'chave')
    search_fields = ('titulo',)
    prepopulated_fields = {'chave': ('titulo',)}

@admin.register(ConteudoInteligencia)
class ConteudoInteligenciaAdmin(admin.ModelAdmin):
    list_display = ('titulo_card', 'categoria', 'titulo_interno')
    list_filter = ('categoria',)
    search_fields = ('titulo_card', 'titulo_interno', 'corpo_texto')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }