from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254)

    def clean_username(self):
        email = self.cleaned_data.get('username')
        User = get_user_model()
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email не зарегистрирован.')
        return email
