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


class Comment(models.Model):
    review = models.ForeignKey('review', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} comment on {self.review.id}"
