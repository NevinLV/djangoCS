# Generated by Django 3.2.9 on 2022-01-22 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='tags',
            field=models.ManyToManyField(related_name='Courses_Tags', to='main.Tags'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='users',
            field=models.ManyToManyField(related_name='Courses_Users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='img',
            name='course',
            field=models.ForeignKey(db_column='Course_id', on_delete=django.db.models.deletion.CASCADE, to='main.courses'),
        ),
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(db_column='Course_id', on_delete=django.db.models.deletion.CASCADE, to='main.courses'),
        ),
        migrations.CreateModel(
            name='CoursesUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(db_column='Course_id', on_delete=django.db.models.deletion.CASCADE, to='main.courses')),
                ('user', models.ForeignKey(db_column='User_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Courses_Users',
            },
        ),
        migrations.CreateModel(
            name='CoursesTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(db_column='Course_id', on_delete=django.db.models.deletion.CASCADE, to='main.courses')),
                ('tag', models.ForeignKey(db_column='Tag_id', on_delete=django.db.models.deletion.CASCADE, to='main.tags')),
            ],
            options={
                'db_table': 'Courses_Tags',
            },
        ),
    ]
