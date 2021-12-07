from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Authors, Profile
from .models import Categories
from .models import CourseTag
from .models import CourseUser
from .models import Courses
from .models import Img
from .models import Users
from .models import Tags
from .models import Video

admin.site.register(Authors)
admin.site.register(Categories)
admin.site.register(CourseTag)
admin.site.register(CourseUser)
admin.site.register(Courses)
admin.site.register(Img)
admin.site.register(Users)
admin.site.register(Tags)
admin.site.register(Video)
admin.site.register(Profile)


# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('avatar_tag',
#                     'user')  # В качестве поля указываем метод, который вернёт тег картинки в списке пользовательских профилей
#     readonly_fields = ['avatar_tag']  # обязательно read only режим
#     fields = ('avatar_tag', 'user')  # Указываем поля, которые нужно отобразить в административной форме
#
#     # Нужна inline форма
# class ProfileInline(admin.StackedInline):
#     model = Profile  # указываем модель профиля
#     can_delete = False  # запрещаем удаление
#     fields = ('avatar_tag',)  # Указываем, какое поле отображать, снова тег аватарки
#     readonly_fields = ['avatar_tag']  # Указываем, что это read only поле
#
#     # Создаём свою форму для отображения пользовательского профиля
# class EUserAdmin(UserAdmin):
#     # Указываем, что будет в качестве inline формы
#     inlines = [
#         ProfileInline
#     ]
#     # модифицируем список отображаемых полей, чтобы увидеть аватарку с остальными полями
#     list_display = ('avatar_tag',) + UserAdmin.list_display
#
#     # а также создаём метод для получения тега аватарки из пользовательского профиля
#     def avatar_tag(self, obj):
#         return obj.userprofile.avatar_tag()
#
# admin.site.register(Profile, UserProfileAdmin)
# admin.site.unregister(User)
# admin.site.register(User, EUserAdmin)
