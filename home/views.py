from django.shortcuts import render
from reviews.models import Review

# Create your views here.


def index(request):

    reviews = Review.objects.filter(approved='approved').order_by('-star_rating')

    return render(request, "home/index.html", {'reviews': reviews})