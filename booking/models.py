from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .utils import create_id

# Create your models here.


class Booking(models.Model):
    APPROVED_CHOICES = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('denied', 'denied'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    duration = models.DurationField(default=timedelta(hours=1), help_text="Length of stay")
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

    # def CalcTime(self, *args, **kwargs):
    #     if self.duration:
    #         start_datetime = datetime.combine(self.booking_date, self.booking_time)
    #         end_datetime = start_datetime + self.duration
    #         self.end_time = end_datetime.time()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} booked for {self.booking_time} on {self.booking_date}"


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Order(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.menu_item.price * item.quantity for item in self.order_items.all())

    def __str__(self):
        return f"Booking - {self.booking}"


class OrderItem(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} X {self.menu_item.name}"
