from django.db import models

class studentregistration(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    photo = models.FileField(upload_to='student_images')
    date_of_reg = models.DateField(auto_now_add=True)


