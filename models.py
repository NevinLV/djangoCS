# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    name = models.CharField()
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Authors'


class Categories(models.Model):
    title = models.CharField()

    class Meta:
        managed = False
        db_table = 'Categories'


class CourseTag(models.Model):
    tag = models.ForeignKey('Tags', models.DO_NOTHING, db_column='Tag_id')  # Field name made lowercase.
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course_Tag'


class CourseUser(models.Model):
    course = models.ForeignKey('Courses', models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course_User'

class Tags(models.Model):
    title = models.CharField()

    class Meta:
        managed = False
        db_table = 'Tags'


class Courses(models.Model):
    title = models.CharField(verbose_name='Название курса')
    description = models.CharField(verbose_name='Описание')
    date = models.TextField(verbose_name='Дата')
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='Category_id',verbose_name='Категория')  # Field name made lowercase.
    author = models.ForeignKey(Authors, models.DO_NOTHING, db_column='Author_id', verbose_name='Автор')  # Field name made lowercase.
    tags = models.ManyToManyField(Tags)

    class Meta:
        managed = False
        db_table = 'Courses'


class Img(models.Model):
    path = models.CharField()
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Img'


class Video(models.Model):
    path = models.CharField()
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Video'
