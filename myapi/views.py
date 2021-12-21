from main.models import Courses, Categories

from rest_framework import viewsets
from myapi.serializers import CoursesSerializer

from rest_framework.response import Response
from rest_framework.views import APIView



class CoursesViewSet(APIView):
    def get(self, request):
        # Получаем набор всех записей из таблицы Capital
        queryset = Courses.objects.all()
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = CoursesSerializer(
            instance=queryset, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)

class GetCoursesInfoView(APIView):
    def get(self, request, category_id):
        # Получаем набор всех записей из таблицы Capital
        queryset = Courses.objects.filter(category_id=category_id)
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = CoursesSerializer(
            instance=queryset, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)

class GetCourseView(APIView):
    def get(self, request, course_id):
        # Получаем набор всех записей из таблицы Capital
        queryset = Courses.objects.filter(id=course_id)
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = CoursesSerializer(
            instance=queryset, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)
