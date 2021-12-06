from django.shortcuts import render
from main.models import Courses

from rest_framework import viewsets
from myapi.serializers import CoursesSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer