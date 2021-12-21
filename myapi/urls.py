from django.urls import path, include
from . import views
from rest_framework import routers

from .views import GetCoursesInfoView, CoursesViewSet, GetCourseView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('/v1/courses/category/<int:category_id>/', GetCoursesInfoView.as_view()),
    path('/v1/courses/all/', CoursesViewSet.as_view()),
    path('/v1/courses/<int:course_id>/', GetCourseView.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
