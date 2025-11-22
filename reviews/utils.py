from .models import Review


def all_reviews():
    return Review.objects.filter(approved='approved').order_by('-star_rating')