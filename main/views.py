from django.shortcuts import render
from .models import Courses, Categories

def main(request):
    categories = Categories.objects.all()
    courses = Courses.objects.all()

    context = {
        'title': 'Главная',
        'categories': categories,
        'courses': courses,
    }
    return render(request, 'main/main.html', context=context)

def show_course(request, course_id):
    course = Courses.objects.filter(id=course_id)

    context = {
        'course': course,
        'title': course[0],
    }

    return render(request, 'main/course.html', context=context)


def show_category(request, category_id):
    categories = Categories.objects.filter(id=category_id)
    courses = Courses.objects.filter(category_id=category_id)

    context = {
        'courses': courses,
        'title': categories[0],
        'category_selected': category_id,
    }

    return render(request, 'main/courses.html', context=context)

