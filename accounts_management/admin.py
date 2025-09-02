# accounts_management/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Importamos o modelo original e os novos modelos proxy
from .models import CustomUser, EmpresaUser, EmpreendedorUser

# Mantemos a classe de admin base que já tínhamos
class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    list_display = ('username', 'email', 'user_type', 'is_staff')
    # Adicionamos um filtro na lateral para facilitar a busca
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'groups')


# --- NOVAS CLASSES E REGISTROS ---

@admin.register(EmpresaUser)
class EmpresaUserAdmin(CustomUserAdmin):
    """
    Classe de Admin específica para exibir apenas usuários do tipo 'Empresa'.
    """
    def get_queryset(self, request):
        # Sobrescrevemos o método get_queryset para filtrar os resultados
        return super().get_queryset(request).filter(user_type='empresa')


@admin.register(EmpreendedorUser)
class EmpreendedorUserAdmin(CustomUserAdmin):
    """
    Classe de Admin específica para exibir apenas usuários do tipo 'Empreendedor'.
    """
    def get_queryset(self, request):
        return super().get_queryset(request).filter(user_type='empreendedor')