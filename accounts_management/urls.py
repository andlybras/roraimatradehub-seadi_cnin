# accounts_management/urls.py

from django.urls import path
# Importamos as views de autenticação prontas do Django
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    
    # URL de Login
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html', # Caminho para o nosso template
        redirect_authenticated_user=True # Redireciona se o usuário já estiver logado
    ), name='login'),
    
    # URL de Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]