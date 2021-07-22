from django.db import models

class StudentRegistration(models.Model):
    name = models.CharField(max_length=40,null=False)
    contact = models.IntegerField(unique=True,null=False)
    email= models.EmailField(max_length=40,unique=True,null=False)
    password = models.CharField(max_length=40,null=False)
    otp = models.IntegerField(default=0000,null=False)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="pending",max_length=40,null=False)



