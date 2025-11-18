from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    path('booking/new/', views.CreateBooking, name='booking_create'),
    path('booking/<str:booking_id>/order/', views.food_order, name='order_food'),
    path('booking/success/<str:booking_id>/', views.BookingSuccess, name='booking_success'),
]