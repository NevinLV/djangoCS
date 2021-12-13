from django.urls import path
from . import views
from .views import show_category, show_course, show_user_page, create_course, search_course, results

urlpatterns = [
    path('', views.main, name='main'),
    path('/course/<int:course_id>/', show_course, name='course'),
    path('/category/<int:category_id>/', show_category, name='category'),
    path('/user/<int:user_id>/', show_user_page, name='user_page'),
    path('/create', create_course, name='create_course'),
    path('/search', search_course, name='search_course'),
    path('/results', results.as_view(), name='results'),
]
