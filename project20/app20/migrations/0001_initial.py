# Generated by Django 3.2.3 on 2021-07-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseModel',
            fields=[
                ('course_no', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
                ('course_fee', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=30)),
                ('student_contact', models.IntegerField()),
                ('student_course', models.ManyToManyField(to='app20.courseModel')),
            ],
        ),
    ]