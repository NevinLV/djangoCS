from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from login.forms import RegisterUserForm
from main.models import Users


# def login(request):
#     return render(request, 'login/login.html')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('main')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        return dict(list(context.items()))

