from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Gender = (
    ('Male','Male'),
    ('Female','Female'),
    ('male','male'),
    ('female','female'),
    ('Others','Othes'))

Payment = (
    ('On-Site','On-Site'),
    ('Online','Online'),
    ('online','online'),
    ('on-site','on-site'),
    ('onsite','onsite'),
    ('Onsite','Onsite'))


class Doctor(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    gender = models.CharField(choices=Gender, default='choose one', max_length=10)
    number = models.CharField(max_length=20)
    licensenum = models.CharField(max_length=30)
    hospital = models.CharField(max_length=50)
    speciality = models.TextField(max_length=100)
    qualification = models.TextField(max_length=100)
    availability = models.CharField(max_length=20)
    start = models.TimeField()
    end = models.TimeField()
    fees = models.CharField(max_length=5)
    percentage = models.CharField(max_length=20)
    profilepic = models.FileField(blank=True, null=True)


