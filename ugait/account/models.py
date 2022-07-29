from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    is_student=models.BooleanField(default=False)
    is_guide=models.BooleanField(default=False)