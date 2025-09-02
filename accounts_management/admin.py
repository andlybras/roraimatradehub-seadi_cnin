from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EmpresaUser, EmpreendedorUser

class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    list_display = ('username', 'email', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'groups')

@admin.register(EmpresaUser)
class EmpresaUserAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(user_type='empresa')

@admin.register(EmpreendedorUser)
class EmpreendedorUserAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(user_type='empreendedor')