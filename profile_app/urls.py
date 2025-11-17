from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    path('profile/', views.test, name='show_profile'),
    path('profile/edit_profile/', views.EditProfile, name='edit_profile'),
    path('profile/bookings/', views.BookingList, name='booking_list'),
    path('profile/bookings/<str:booking_id>/', views.BookingDetails, name='booking_details'),
    path('profile/bookings/<str:booking_id>/cancel', views.BookingCancel, name='booking_cancel'),
    path('profile/bookings/<str:booking_id>/edit', views.BookingEdit, name='booking_edit'),
]
