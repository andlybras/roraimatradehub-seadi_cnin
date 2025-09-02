from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Campo de tipo de perfil, sem valor inicial
    user_type = forms.ChoiceField(
        label="Este perfil é para:",
        choices=CustomUser.USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
    )

    # Outros campos que já tínhamos
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={'placeholder': 'ex: jose.silva_rr'})
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'ex: seuemail@dominio.com'}),
        help_text="O e-mail deve ser único e válido."
    )
    email2 = forms.EmailField(
        label="Confirmação de e-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'Confirme seu e-mail'})
    )

    # ADICIONANDO OS CAMPOS DE SENHA EXPLICITAMENTE
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Crie uma senha forte'})
    )
    password2 = forms.CharField(
        label="Confirmação de senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('user_type', 'username', 'email', 'email2')

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email and email2 and email != email2:
            raise forms.ValidationError("Os e-mails não são iguais.")
        return email2