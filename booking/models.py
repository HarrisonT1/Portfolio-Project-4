from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    comments = models.TextField(blank=True)
    number_of_people = models.PositiveIntegerField()