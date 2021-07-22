from django.db import models

class courseModel(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    course_fee = models.FloatField()

class studentModel(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=30)
    student_contact = models.IntegerField()
    student_course = models.ManyToManyField(courseModel)
