from django.shortcuts import render
from reviews.models import Review

# Create your views here.


def index(request):

    reviews = Review.objects.filter(
        approved='approved', star_rating__gte=4).order_by('?')[:4]

    return render(request, "home/index.html", {'reviews': reviews})


def menu(request):
    return render(request, "home/menu.html")
