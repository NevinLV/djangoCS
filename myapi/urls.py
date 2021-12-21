from django.urls import path, include
from . import views
from rest_framework import routers

from .views import GetCoursesInfoView, CoursesViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('/v1/category/<int:category_id>/', GetCoursesInfoView.as_view()),
    path('/v1/all', CoursesViewSet.as_view()),
    # path('/user/<int:user_id>/', show_user_page,),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
