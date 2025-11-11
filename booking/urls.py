from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    path('booking/new/', views.CreateBooking, name='booking_create'),
    path('bookings/', views.BookingList, name='booking_list'),
]