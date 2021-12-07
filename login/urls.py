from django.urls import path
from . import views
from .views import LoginUser, RegisterUser

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('/registration', RegisterUser.as_view(), name='registration'),
]
