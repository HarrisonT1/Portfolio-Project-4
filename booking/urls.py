from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    path(
        'booking/new/',
        views.create_booking,
        name='booking_create'),

    path(
        'booking/success/<str:booking_id>/',
        views.booking_success,
        name='booking_success'),
]
