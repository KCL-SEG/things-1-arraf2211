from django.db import models

# Create your models here.

class User(AbstractUser):
    name = models.TextField(blank = False)
    description = models.TextField(blank = True)
    quantity = models.IntegerField(blank = False)
