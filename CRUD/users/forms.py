from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import MyUser

class RegistartionForm(UserCreationForm):
    email = forms.EmailField(max_length=20)

    class Meta:
        model = MyUser
        fields = (
            'email',
            'phone_number',
            'password1',
            'password2',
        )

        

