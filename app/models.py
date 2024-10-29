from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60)
    adm_no = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='profiles', default='default.jpg')

