import requests
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import AddCourseForm, SearchCourseForm
from .models import *
from django.contrib.auth.models import User
import datetime

now = datetime.datetime.now()


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
    all_categories = Categories.objects.all()

    user = request.user
    author = Authors.objects.filter(user_id=user.id)

    if not author.exists():
        Authors.objects.create(name=user, user_id=user.id)
        author = Authors.objects.filter(user_id=user.id)

    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        course = form.save(commit=False)
        course.author = author[0]
        course.date = now.strftime("%d.%m.%Y")


        if form.is_valid():
            try:
                course.save()

                tags = form.cleaned_data.get('tags')
                tags_list = tags.lower().split(', ')

                for t in tags_list:
                    tag = Tags.objects.filter(title=t)
                    if not tag.exists():
                        Tags.objects.create(title=t)
                        tag = Tags.objects.filter(title=t)

                    course.save()
                    course.tags.add(tag[0])

                return redirect('main')
            except:
                form.add_error(None, 'Ошибка добавления курса')
    else:
        form = AddCourseForm()

    context = {
        'form': form,
        'title': 'Создание курса',
        'categories': all_categories,
    }
    return render(request, 'main/createcourse.html', context=context)


def show_course(request, course_id):
    course = Courses.objects.filter(id=course_id)
    all_categories = Categories.objects.all()

    user = request.user
    user_has_course = Courses.objects.filter(users__id=user.id, id=course_id)

    print(user_has_course)

    context = {
        'categories': all_categories,
        'course': course,
        'title': course[0],
        'user_has_course': user_has_course,
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


def search_course(request):
    all_categories = Categories.objects.all()

    context = {
        'title': 'Поиск',
        'categories': all_categories,
    }
    return render(request, 'main/search.html', context=context)


class advanced_results(ListView):
    model = Courses
    template_name = 'main/results.html'


    def get_queryset(self):
        title = self.request.GET.get('title', default='')
        desk = self.request.GET.get('desk', default='')
        cat = self.request.GET.get('cat', default='')
        author = self.request.GET.get('author', default='')

        if cat == 'Категория':
            cat = ''

        object_list = Courses.objects.filter(
            Q(title__icontains=title) &
            Q(description__icontains=desk) &
            Q(category__title__icontains=cat) &
            Q(author__name__icontains=author)
        )

        return object_list


class results(ListView):
    model = Courses
    template_name = 'main/results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Courses.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__name__icontains=query)
        )

        return object_list



