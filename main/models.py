from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from django.conf import settings


class Authors(models.Model):
    name = models.CharField('name', max_length=80, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Authors'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, )
    surname = models.CharField('surname', max_length=80, null=False)
    name = models.CharField('name', max_length=80, null=False)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    birth_date = models.DateField(null=True, blank=True)

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    class Meta:
        db_table = 'Profile'

    def __str__(self):
        return self.name


class Categories(models.Model):
    title = models.CharField('title', max_length=30, null=False)

    class Meta:
        db_table = 'Categories'


    def __str__(self):
        return self.title

class Tags(models.Model):
    title = models.TextField('path')

    class Meta:
        db_table = 'Tags'

    def __str__(self):
        return self.title

class Courses(models.Model):
    title = models.CharField('title', max_length=80, null=False)
    description = models.TextField('description')
    date = models.TextField('date')
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='Category_id')  # Field name made lowercase.
    author = models.ForeignKey(Authors, models.DO_NOTHING, db_column='Author_id')  # Field name made lowercase.
    # tags = models.ManyToManyField(Tags, related_name="Courses_Tags")
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Courses_Users")

    class Meta:
        db_table = 'Courses'

    def __str__(self):
        return self.title


class CoursesTags(models.Model):
    tag = models.ForeignKey('Tags', on_delete=models.CASCADE, db_column='Tag_id')  # Field name made lowercase.
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Courses_Tags'



class CoursesUsers(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, db_column='Course_id')  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='User_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Courses_Users'


class Img(models.Model):
    path = models.TextField('path')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Img'


class Video(models.Model):
    path = models.TextField('path')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Video'

