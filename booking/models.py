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

    def __str__(self):
        return f"{self.first_name} {self.last_name} booked for {self.booking_time} on {self.booking_date}"
