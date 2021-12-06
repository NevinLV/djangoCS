from django.urls import path
from . import views
from .views import show_category, show_course

urlpatterns = [
    path('', views.main, name='main'),
    path('/course/<int:course_id>/', show_course, name='course'),
    path('/category/<int:category_id>/', show_category, name='category'),
]
