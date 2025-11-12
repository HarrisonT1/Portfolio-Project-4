from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    duration = models.DurationField(default=timedelta(hours=1), help_text="Length of stay")
    comments = models.TextField(blank=True)
    number_of_people = models.PositiveIntegerField()

    def CalcTime(self, *args, **kwargs):
        if self.duration:
            start_datetime = datetime.combine(self.booking_date, self.booking_time)
            end_datetime = start_datetime + self.duration
            self.end_time = end_datetime.time()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.first_name} {self.last_name} booked for {self.booking_time} on {self.booking_date}"
