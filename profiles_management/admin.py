from django.contrib import admin
from .models import CNAE, EmpresaProfile, EmpreendedorProfile

@admin.register(CNAE)
class CNAEAdmin(admin.ModelAdmin):
    """
    Configuração do Admin para o modelo CNAE.
    Adiciona uma barra de busca para facilitar encontrar códigos.
    """
    search_fields = ['codigo', 'descricao']
    list_display = ['codigo', 'descricao']

@admin.register(EmpresaProfile)
class EmpresaProfileAdmin(admin.ModelAdmin):
    """
    Configuração do Admin para o Perfil de Empresa.
    Mostra informações importantes na lista e permite a busca.
    """
    list_display = ['nome_fantasia', 'cnpj', 'user', 'responsavel_nome']
    search_fields = ['nome_fantasia', 'cnpj', 'razao_social', 'user__username']
    list_filter = ['uf', 'cidade']

@admin.register(EmpreendedorProfile)
class EmpreendedorProfileAdmin(admin.ModelAdmin):
    """
    Configuração do Admin для o Perfil de Empreendedor.
    """
    list_display = ['nome_completo', 'cpf', 'user', 'area_atuacao']
    search_fields = ['nome_completo', 'cpf', 'user__username']
    list_filter = ['estado', 'cidade']