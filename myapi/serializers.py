from rest_framework import serializers

from main.models import *


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ('title', 'description', 'date', 'category_id', 'author_id')
