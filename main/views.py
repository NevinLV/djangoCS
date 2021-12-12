import requests
from django.shortcuts import render, redirect

from .forms import AddCourseForm
from .models import *
from django.contrib.auth.models import User

def main(request):
    categories = Categories.objects.all()
    courses = Courses.objects.all()

    context = {
        'title': 'Главная',
        'categories': categories,
        'courses': courses,
    }
    return render(request, 'main/main.html', context=context)


def create_course(request):
    user = request.user
    author = Authors.objects.filter(user_id=user.id)
    if author.exists():
        print(author)
    else:
        Authors.objects.create(name=user, user_id=user.id)
    print(author)

    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            try:
                Courses.objects.create(**form.cleaned_data)
                return redirect('main')
            except:
                form.add_error(None, 'Ошибка добавления курса')
    else:
        form = AddCourseForm()

    context = {
        'form': form,
        'title': 'Создание курса',

    }
    return render(request, 'main/createcourse.html', context=context)


def show_course(request, course_id):
    course = Courses.objects.filter(id=course_id)
    all_categories = Categories.objects.all()

    context = {
        'categories': all_categories,
        'course': course,
        'title': course[0],
    }

    return render(request, 'main/course.html', context=context)


def show_category(request, category_id):
    course = Categories.objects.all()
    categories = Categories.objects.filter(id=category_id)
    all_categories = Categories.objects.all()
    courses = Courses.objects.filter(category_id=category_id)

    context = {
        'categories': all_categories,
        'course': course,
        'courses': courses,
        'title': categories[0],
        'category_selected': category_id,
    }

    return render(request, 'main/courses.html', context=context)

def show_user_page(request, user_id):
    user = User.objects.filter(id=user_id)

    context = {
        'title': user[0],
    }

    return render(request, 'main/userpage.html', context=context)


