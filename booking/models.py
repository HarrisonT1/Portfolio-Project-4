from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .utils import create_id

# Create your models here.


class Booking(models.Model):
    APPROVED_CHOICES = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('denied', 'denied'),
    ]

    limit_letters = RegexValidator(
        r'^[a-zA-Z]+$', 'You may only use characters for this field')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    first_name = models.CharField(max_length=50, validators=[limit_letters])
    last_name = models.CharField(max_length=50, validators=[limit_letters])
    email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    comments = models.TextField(blank=True)
    number_of_people = models.PositiveIntegerField()
    booking_id = models.CharField(
        max_length=7,
        unique=True,
        editable=False,
        default=create_id,
        null=False,
        )
    approved = models.CharField(
        max_length=10,
        choices=APPROVED_CHOICES,
        default='pending'
    )

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}"
            f"booked for {self.booking_time} on {self.booking_date}")
