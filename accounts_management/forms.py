from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = EmailField(label="E-mail")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('user_type', 'username', 'email')