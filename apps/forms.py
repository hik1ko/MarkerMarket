from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data['password'])
