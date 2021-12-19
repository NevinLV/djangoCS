from rest_framework import serializers

from main.models import *


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ('title', 'description', 'date', 'category', 'author')

    author = serializers.SerializerMethodField('get_author_name')

    def get_author_name(self, obj):
        return obj.author.name

    category = serializers.SerializerMethodField('get_categ_title')

    def get_categ_title(self, obj):
        return obj.category.title


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ('title', 'description', 'date', 'category', 'author')

    author = serializers.SerializerMethodField('get_author_name')

    def get_author_name(self, obj):
        return obj.author.name

    category = serializers.SerializerMethodField('get_categ_title')

    def get_categ_title(self, obj):
        return obj.category.title