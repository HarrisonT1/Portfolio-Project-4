from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    path('profile/bookings/', views.BookingList, name='booking_list'),
    path('profile/bookings/<booking_id>', views.BookingDetails, name='profile'),
]
