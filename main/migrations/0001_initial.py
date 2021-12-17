# Generated by Django 3.2.9 on 2021-12-13 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('user', models.ForeignKey(db_column='User_id', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
            ],
            options={
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('date', models.TextField(verbose_name='date')),
                ('author', models.ForeignKey(db_column='Author_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.authors')),
                ('category', models.ForeignKey(db_column='Category_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.categories')),
            ],
            options={
                'db_table': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='path')),
            ],
            options={
                'db_table': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(verbose_name='path')),
                ('course', models.ForeignKey(db_column='Course_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.courses')),
            ],
            options={
                'db_table': 'Video',
            },
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(verbose_name='path')),
                ('course', models.ForeignKey(db_column='Course_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.courses')),
            ],
            options={
                'db_table': 'Img',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='tags',
            field=models.ManyToManyField(related_name='course_tags', to='main.Tags'),
        ),
        migrations.AddField(
            model_name='courses',
            name='users',
            field=models.ManyToManyField(related_name='course_users', to=settings.AUTH_USER_MODEL),
        ),
    ]