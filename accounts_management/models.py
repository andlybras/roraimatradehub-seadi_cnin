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
    class Meta:
        proxy = True
        verbose_name = 'Perfil Empresarial - Empresa'
        verbose_name_plural = 'Perfis Empresariais - Empresa'

class EmpreendedorUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Perfil Empresarial - Empreendedor'
        verbose_name_plural = 'Perfis Empresariais - Empreendedor'