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


class Categories(models.Model):
    title = models.CharField('title', max_length=30, null=False)

    class Meta:
        db_table = 'Categories'

    def __str__(self):
        return self.title


class CourseTag(models.Model):
    tag = models.ForeignKey('Tags', models.DO_NOTHING, db_column='Tag_id')  # Field name made lowercase.
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Course_Tag'


class CourseUser(models.Model):
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Course_User'


class Courses(models.Model):
    title = models.CharField('title', max_length=80, null=False)
    description = models.TextField('description')
    date = models.TextField('date')
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='Category_id')  # Field name made lowercase.
    author = models.ForeignKey(Authors, models.DO_NOTHING, db_column='Author_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Courses'

    def __str__(self):
        return self.title


class Img(models.Model):
    path = models.TextField('path')
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Img'


class Tags(models.Model):
    title = models.TextField('path')

    class Meta:
        db_table = 'Tags'

    def __str__(self):
        return self.name


class Video(models.Model):
    path = models.TextField('path')
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Video'

