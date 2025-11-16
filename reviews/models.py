from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    APPROVED_CHOICES = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('denied', 'denied'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    star_rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=5
    )
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.CharField(
        max_length=10,
        choices=APPROVED_CHOICES,
        default='pending'
    )
