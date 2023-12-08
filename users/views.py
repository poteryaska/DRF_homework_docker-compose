from django.shortcuts import render

from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetDoneView

from users.models import User

class LoginView(BaseLoginView):
    template_name = 'users/login.html'