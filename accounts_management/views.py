from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from site_setup.models import HeaderLogo, PartnerLogo

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_logos'] = HeaderLogo.objects.all()
        context['partner_logos'] = PartnerLogo.objects.all().order_by('order')
        
        return context