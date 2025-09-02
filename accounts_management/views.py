# accounts_management/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from site_setup.models import HeaderLogo, PartnerLogo

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_logos'] = HeaderLogo.objects.all()
        context['partner_logos'] = PartnerLogo.objects.all().order_by('order')
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        response = super().form_valid(form)
        return response

    # --- MÉTODO "DETETIVE" ADICIONADO ---
    def form_invalid(self, form):
        """
        Este método é chamado quando a validação do formulário falha.
        Vamos usá-lo para imprimir os erros no terminal.
        """
        print("--- ERROS DE VALIDAÇÃO ENCONTRADOS ---")
        # O .as_json() formata todos os erros de uma maneira fácil de ler.
        print(form.errors.as_json())
        print("------------------------------------")
        
        # Continua com o comportamento normal, que é recarregar a página.
        return super().form_invalid(form)