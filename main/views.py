import requests
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView

from django.core.serializers import serialize
from django.http import HttpResponse

from .forms import *
from .models import *
from django.contrib.auth.models import User
import datetime

now = datetime.datetime.now()


def main(request):
    categories = Categories.objects.all()
    courses = Courses.objects.all()
    course_tags = CoursesTags.objects.all()
    course_users = CoursesUsers.objects.values('course_id').annotate(total=Count('id'))

    context = {
        'title': 'Все курсы',
        'categories': categories,
        'courses': courses,
        'tags': course_tags,
        'count_users': course_users,
    }
    return render(request, 'main/main.html', context=context)

def home(request):
    categories = Categories.objects.all()
    courses = Courses.objects.all()
    course_tags = CoursesTags.objects.all()
    course_users = CoursesUsers.objects.values('course_id').annotate(total=Count('id'))

    author_users_count = CoursesUsers.objects.values('course__author__user_id').annotate(total=Count('id')).order_by('-total')[:3]
    author_users_count_list = list(author_users_count)
    top_authors = []
    for user in author_users_count_list:
        top_authors.append(User.objects.get(id=user['course__author__user_id']))

    course_users_count = CoursesUsers.objects.values('course_id').annotate(total=Count('id')).order_by('-total')[:3]
    course_users_count_list = list(course_users_count)
    top_course = []
    for course in course_users_count_list:
        top_course.append(Courses.objects.get(id=course['course_id']))


    context = {
        'title': 'Главная',
        'categories': categories,
        'courses': courses,
        'tags': course_tags,
        'count_users': course_users,
        'top_authors': top_authors,
        'top_course' : top_course,
    }
    return render(request, 'main/home.html', context=context)


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

                    course.save()

                    tag = Tags.objects.get(title=t).id
                    coursetag = CoursesTags(tag_id=tag, course_id=course.id)
                    coursetag.save()

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


def edit_course(request, course_id):
    user = request.user
    all_categories = Categories.objects.all()
    selCourse = Courses.objects.filter(id=course_id)
    selectCourse = Courses.objects.get(id=course_id)
    course_tags = CoursesTags.objects.all()

    if user == selectCourse.author.user or user.is_superuser:
        if request.method == 'POST':
            selectCourse.title = request.POST.get('title')
            selectCourse.description = request.POST.get('desk')
            category = request.POST.get('cat')
            selectCourse.category = Categories.objects.get(title=category)
            selectCourse.save()

            try:
                tags = request.POST.get('tags')
                tags_list = tags.lower().split(', ')

                for t in tags_list:
                    tag = Tags.objects.filter(title=t)
                    if not tag.exists():
                        Tags.objects.create(title=t)
                        tag = Tags.objects.filter(title=t)

                    if t != '':
                        if not CoursesTags.objects.filter(tag__title=t, course_id=selectCourse.id).exists():
                            tag = Tags.objects.get(title=t).id
                            coursetag = CoursesTags(tag_id=tag, course_id=selectCourse.id)
                            coursetag.save()
                    selectCourse.save()

                return redirect('main')
            except:
                print("Ой, что-то пошло не так")

        else:
            form = EditCourseForm()


        form = EditCourseForm()
        context = {
            'form': form,
            'title': 'Редактирование курса',
            'categories': all_categories,
            'course': selCourse,
            'tags': course_tags,
        }
        return render(request, 'main/editcourse.html', context=context)
    else:
        context = {
            'title': 'Ошибка доступа',
            'categories': all_categories,
        }
        return render(request, 'main/accessisdenied.html', context=context)

def show_course(request, course_id):
    course = Courses.objects.filter(id=course_id)
    all_categories = Categories.objects.all()
    course_tags = CoursesTags.objects.filter(course_id=course_id)

    user = request.user
    user_has_course = CoursesUsers.objects.filter(course_id=course_id, user_id=user.id)
    course_users = CoursesUsers.objects.values('course_id').annotate(total=Count('id'))



    context = {
        'categories': all_categories,
        'courses': course,
        'title': course[0],
        'user_has_course': user_has_course,
        'tags': course_tags,
        'count_users': course_users,
    }

    return render(request, 'main/course.html', context=context)

def show_all_category(request):
    all_categories = Categories.objects.all()

    context = {
        'categories': all_categories,
        'title': 'Категории',
    }

    return render(request, 'main/categories.html', context=context)


def show_category(request, category_id):
    course = Categories.objects.all()
    categories = Categories.objects.filter(id=category_id)
    all_categories = Categories.objects.all()
    courses = Courses.objects.filter(category_id=category_id)
    course_tags = CoursesTags.objects.all()
    course_users = CoursesUsers.objects.values('course_id').annotate(total=Count('id'))

    context = {
        'categories': all_categories,
        'course': course,
        'courses': courses,
        'title': categories[0],
        'category_selected': category_id,
        'tags': course_tags,
        'count_users': course_users,
    }

    return render(request, 'main/courses.html', context=context)


def show_user_page(request, user_id):
    userProfile = User.objects.filter(id=user_id)
    print(userProfile)
    course_users = CoursesUsers.objects.values('course_id').annotate(total=Count('id'))

    author_course = Courses.objects.filter(author__user_id=user_id)
    sub_course = Courses.objects.filter(coursesusers__user_id=user_id)

    course_tags = CoursesTags.objects.all()

    context = {
        'author_course': author_course,
        'sub_course': sub_course,
        'title': userProfile[0],
        'count_users': course_users,
        'tags': course_tags,
        'userProfile': userProfile[0],
    }

    return render(request, 'main/userpage.html', context=context)


def search_course(request):
    all_categories = Categories.objects.all()

    context = {
        'title': 'Поиск',
        'categories': all_categories,
    }
    return render(request, 'main/search.html', context=context)

class course_filter(ListView):
    model = Courses
    template_name = 'main/results.html'


    def get_queryset(self):
        title = self.request.GET.get('title', default='')
        desk = self.request.GET.get('desk', default='')
        cat = self.request.GET.get('cat', default='')
        author = self.request.GET.get('author', default='')
        tags = self.request.GET.get('tags', default='')

        if cat == 'Категория':
            cat = ''

        tags_list = tags.lower().split(', ')
        if tags_list == ['']:
            object_list = Courses.objects.filter(
                Q(title__icontains=title) &
                Q(description__icontains=desk) &
                Q(category__title__icontains=cat) &
                Q(author__name__icontains=author)
            ).distinct()
        else:
            courses_has_tag = CoursesTags.objects.filter(Q(tag__title__in=tags_list))
            courses = []
            for el in courses_has_tag:
                courses.append(el.course.id)

            print(courses)
            object_list = Courses.objects.filter(
                Q(title__icontains=title) &
                Q(description__icontains=desk) &
                Q(category__title__icontains=cat) &
                Q(author__name__icontains=author) &
                Q(id__in=courses)
            ).distinct()

        return object_list

class advanced_results(ListView):
    model = Courses
    template_name = 'main/results.html'


    def get_queryset(self):
        title = self.request.GET.get('title', default='')
        desk = self.request.GET.get('desk', default='')
        cat = self.request.GET.get('cat', default='')
        author = self.request.GET.get('author', default='')
        tags = self.request.GET.get('tags', default='')

        if cat == 'Категория':
            cat = ''

        tags_list = tags.lower().split(', ')
        if tags_list == ['']:
            object_list = Courses.objects.filter(
                Q(title__icontains=title) &
                Q(description__icontains=desk) &
                Q(category__title__icontains=cat) &
                Q(author__name__icontains=author)
            ).distinct()
        else:
            courses_has_tag = CoursesTags.objects.filter(Q(tag__title__in=tags_list))
            courses = []
            for el in courses_has_tag:
                courses.append(el.course.id)

            # print(courses)
            object_list = Courses.objects.filter(
                Q(title__icontains=title) &
                Q(description__icontains=desk) &
                Q(category__title__icontains=cat) &
                Q(author__name__icontains=author) &
                Q(id__in=courses)
            ).distinct()

        print('object_list: ')
        print(object_list)
        return object_list


class results(ListView):
    model = Courses
    template_name = 'main/results.html'

    def get_queryset(self):
        categories = Categories.objects.all()
        course_tags = CoursesTags.objects.all()
        course_users = CoursesUsers.objects.values('course_id').annotate(total=Count('id'))

        query = self.request.GET.get('q')

        tags = query
        tags_list = tags.lower().split(', ')
        courses_has_tag = CoursesTags.objects.filter(Q(tag__title__in=tags_list))
        courses = []
        for el in courses_has_tag:
            courses.append(el.course.id)

        object_list = Courses.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(id__in=courses)
        ).distinct()

        context = {
            'title': 'Главная',
            'categories': categories,
            'object_list': object_list,
            'tags': course_tags,
            'count_users': course_users,
        }

        return object_list


def delete_course(request, course_id):
    user = request.user
    selectCourse = Courses.objects.get(id=course_id)
    all_categories = Categories.objects.all()
    if user == selectCourse.author.user or user.is_superuser or course_id == 23:
        qs = Courses.objects.filter(id=course_id)
        data = serialize("json", qs, fields=['title', 'description', 'category', 'date', 'author'])

        Courses.objects.get(id=course_id).delete()

        return HttpResponse(data, content_type="application/json")
        #return redirect('main')
    else:
        context = {
            'title': 'Ошибка доступа',
            'categories': all_categories,
        }
        return render(request, 'main/accessisdenied.html', context=context)


def sub_course(request, course_id):
    user = request.user
    usercourse = CoursesUsers(user_id=user.id, course_id=course_id)
    usercourse.save()
    return redirect('course', course_id)

def unsub_course(request, course_id):
    user = request.user
    CoursesUsers.objects.get(user_id=user.id, course_id=course_id).delete()

    return redirect('course', course_id)



