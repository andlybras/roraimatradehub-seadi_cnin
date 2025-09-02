from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('empresa', 'Empresa'),
        ('empreendedor', 'Empreendedor'),
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='empreendedor',
        verbose_name="Este perfil é para"
    )
    
class EmpresaUser(CustomUser):
    """
    Modelo Proxy para filtrar e exibir apenas usuários do tipo 'Empresa'.
    """
    class Meta:
        # Define este modelo como um proxy. Nenhuma nova tabela será criada.
        proxy = True
        # Nomes que aparecerão no painel de administração
        verbose_name = 'Perfil Empresarial - Empresa'
        verbose_name_plural = 'Perfis Empresariais - Empresa'


class EmpreendedorUser(CustomUser):
    """
    Modelo Proxy para filtrar e exibir apenas usuários do tipo 'Empreendedor'.
    """
    class Meta:
        proxy = True
        verbose_name = 'Perfil Empresarial - Empreendedor'
        verbose_name_plural = 'Perfis Empresariais - Empreendedor'