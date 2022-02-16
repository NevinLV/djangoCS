from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/home', views.home, name='home'),
    path('', views.main, name='main'),
    path('/categories', show_all_category, name='categories'),
    path('/course/<int:course_id>/', show_course, name='course'),
    path('/course/<int:course_id>/edit', edit_course, name='edit_course'),
    path('/course/<int:course_id>/delete', delete_course, name='delete_course'),
    path('/course/<int:course_id>/sub', sub_course, name='sub_course'),
    path('/course/<int:course_id>/unsub', unsub_course, name='unsub_course'),
    path('/category/<int:category_id>/', show_category, name='category'),
    path('/user/<int:user_id>/', show_user_page, name='user_page'),
    path('/create', create_course, name='create_course'),
    path('/search', search_course, name='search_course'),
    path('/results', advanced_results.as_view(), name='adv_results'),
    path('/fastresults', results.as_view(), name='results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

