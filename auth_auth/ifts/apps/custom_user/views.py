from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.custom_user.models import CustomUser


class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    template_name = 'logged_out.html'


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
