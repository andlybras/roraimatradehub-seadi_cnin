from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ResendActivationEmailForm
from django.contrib.auth import views as auth_views
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
    success_url = reverse_lazy('account_activation_sent')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
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
            from_email=None, 
            recipient_list=[user.email],
        )
        return redirect(self.success_url)


class CustomLoginView(auth_views.LoginView):
    def form_valid(self, form):
        user = form.get_user()
        if user.is_email_verified:
            return super().form_valid(form)
        else:
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
    return render(request, 'accounts/dashboard.html')


def resend_activation_email(request):
    if request.method == 'POST':
        form = ResendActivationEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user = None

            if user:
                if user.is_active:
                    return redirect('account_already_active')
                else:
                    subject = 'Ative sua conta no Roraima Trade Hub (Novo Link)'
                    message = render_to_string('emails/account_activation_email.html', {
                        'user': user,
                        'domain': request.META['HTTP_HOST'],
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    send_mail(subject, message, None, [user.email])
            
            return redirect('account_activation_sent')
    else:
        form = ResendActivationEmailForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/resend_activation.html', context)