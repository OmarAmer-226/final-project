from django.db import models

# Create your models here.

class Book_Table(models.Model):

    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 11)
    date = models.DateField()
    time = models.TimeField()
    person = models.PositiveSmallIntegerField()
