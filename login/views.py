from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from login.forms import RegisterUserForm, CreateProfileForm, UserLoginForm
from main.models import Profile


class LoginUser(LoginView):
    form_class = UserLoginForm
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
    success_url = reverse_lazy('regprofile')

    def form_valid(self, form):
        valid = super(RegisterUser, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        return dict(list(context.items()))


class CreateProfilePageView(CreateView):
    form_class = CreateProfileForm
    template_name = 'login/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('main')

