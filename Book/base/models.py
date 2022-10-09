from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Data(models.Model):
     first_name = models.CharField(max_length=100)
     last_name =models.CharField(max_length=100)
     age = models.PositiveIntegerField(default=0)

     def __str__(self):
          return self.first_name
