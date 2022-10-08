from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Thing(AbstractUser):
    name = models.TextField(blank = False, max_length = 30)
    description = models.TextField(blank = True,max_length = 120)
    quantity = models.IntegerField(blank = False, max_value = 100)
