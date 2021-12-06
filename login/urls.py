from django.urls import path
from . import views
from .views import LoginUser

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('/registration', LoginUser.as_view(), name='registration'),
]
