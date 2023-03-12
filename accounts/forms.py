from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data.get("username")
        username_exists = User.objects.filter(username__iexact=username).exists()

        if username_exists:
            raise ValidationError("Esse nome de usuário já está em uso!")

        return username
