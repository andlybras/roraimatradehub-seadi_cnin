# accounts_management/views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,  ResendActivationEmailForm
from site_setup.models import HeaderLogo, PartnerLogo
from django.contrib.auth import views as auth_views

# --- NOVAS IMPORTAÇÕES PARA O ENVIO DE E-MAIL ---
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from .models import CustomUser

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    # Após o registro, vamos para uma nova página de "verifique seu e-mail"
    success_url = reverse_lazy('account_activation_sent')

    def form_valid(self, form):
        # 1. Salva o usuário mas não o insere no banco ainda
        user = form.save(commit=False)
        # 2. Marca o usuário como 'inativo' até que o e-mail seja confirmado
        user.is_active = False
        user.save()

        # 3. Lógica para enviar o e-mail de ativação
        subject = 'Ative sua conta no Roraima Trade Hub'
        message = render_to_string('emails/account_activation_email.html', {
            'user': user,
            'domain': self.request.META['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        
        send_mail(
            subject=subject,
            message=message,
            from_email=None,  # Usará o e-mail padrão do settings.py
            recipient_list=[user.email],
        )

        # 4. Redireciona o usuário para a página de sucesso
        return redirect(self.success_url)


class CustomLoginView(auth_views.LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_logos'] = HeaderLogo.objects.all()
        context['partner_logos'] = PartnerLogo.objects.all().order_by('order')
        return context
    
    def form_valid(self, form):
        """
        Esta função é chamada após o Django confirmar que o usuário e a senha estão corretos.
        """
        user = form.get_user()

        # Verificamos nosso campo personalizado 'is_email_verified'
        if user.is_email_verified:
            # Se o e-mail foi verificado, permite o login normalmente.
            return super().form_valid(form)
        else:
            # Se não, adiciona um erro ao formulário e o exibe novamente.
            form.add_error(None, "Sua conta ainda não foi ativada. Por favor, verifique seu e-mail.")
            return self.form_invalid(form)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_email_verified = True
        user.save()
        return redirect('account_activation_valid')
    else:
        return redirect('account_activation_invalid')

@login_required
def dashboard(request):
    context = {
        'header_logos': HeaderLogo.objects.all(),
        'partner_logos': PartnerLogo.objects.all().order_by('order'),
    }
    return render(request, 'accounts/dashboard.html', context)

def resend_activation_email(request):
    if request.method == 'POST':
        form = ResendActivationEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Tenta encontrar um usuário com o e-mail fornecido
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user = None

            if user:
                # Se o usuário existir, verifica se ele já está ativo
                if user.is_active:
                    # Se já estiver ativo, redireciona para a nova página
                    return redirect('account_already_active')
                else:
                    # Se não estiver ativo, envia o novo link
                    subject = 'Ative sua conta no Roraima Trade Hub (Novo Link)'
                    message = render_to_string('emails/account_activation_email.html', {
                        'user': user,
                        'domain': request.META['HTTP_HOST'],
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    send_mail(subject, message, None, [user.email])
            
            # Em caso de sucesso (ou se o e-mail não existir), vai para a pág de "enviado"
            return redirect('account_activation_sent')
    else:
        form = ResendActivationEmailForm()

    context = {
        'form': form,
        'header_logos': HeaderLogo.objects.all(),
        'partner_logos': PartnerLogo.objects.all().order_by('order'),
    }
    return render(request, 'accounts/resend_activation.html', context)