"""
This file powers creation of all forms. You will need to modify
the SignUpForm in order to start collecting the distinct_id.
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import HiddenInput


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets={'username': HiddenInput()}

class LoginForm(AuthenticationForm):
    pass
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password')
        widgets={'username': HiddenInput()}
