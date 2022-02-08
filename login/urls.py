from django.urls import path
from . import views
from .views import LoginUser, RegisterUser, CreateProfilePageView

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('/registration', RegisterUser.as_view(), name='registration'),
    path('/create_profile_page', CreateProfilePageView.as_view(), name='regprofile'),
]
