# accounts_management/views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from site_setup.models import HeaderLogo, PartnerLogo # 1. IMPORTAR OS MODELOS

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home') # Alterado para 'home' após o registro

    # 2. ADICIONAR ESTE MÉTODO
    def get_context_data(self, **kwargs):
        # Primeiro, pega o contexto que a view já gera (com o formulário)
        context = super().get_context_data(**kwargs)
        
        # Agora, adiciona nossas informações extras
        context['header_logos'] = HeaderLogo.objects.all()
        context['partner_logos'] = PartnerLogo.objects.all().order_by('order')
        
        # Retorna o contexto completo para o template
        return context