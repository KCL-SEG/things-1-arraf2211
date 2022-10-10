from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Thing(AbstractUser):
    name = models.CharField(blank = False, max_length = 30, unique = True)
    description = models.CharField(max_length = 120, unique = False, blank = True)
    quantity = models.IntegerField(blank = False,
           validators=[ MaxValueValidator(100),
                        MinValueValidator(0)         
               ]
            )
