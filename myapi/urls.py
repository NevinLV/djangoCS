from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'/v1', views.CoursesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('/it', views.CategoryViewSet),
    # path('/math', views.CategoryViewSet),
    # path('/physics', views.CategoryViewSet),
    # path('/chemistry', views.CategoryViewSet),
    # path('/medicine', views.CategoryViewSet),
    # path('/languages', views.CategoryViewSet),
    # path('/art', views.CategoryViewSet),
    # path('/cooking', views.CategoryViewSet),
    # path('/other', views.CategoryViewSet),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
