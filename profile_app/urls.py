from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    # GENERAL
    path('profile/', views.profile, name='show_profile'),
    path('profile/edit_profile/', views.EditProfile, name='edit_profile'),
    # BOOKINGS
    path('profile/bookings/', views.BookingList, name='booking_list'),
    path('profile/bookings/<str:booking_id>/', views.BookingDetails, name='booking_details'),
    path('profile/bookings/<str:booking_id>/cancel', views.BookingCancel, name='booking_cancel'),
    path('profile/bookings/<str:booking_id>/edit', views.BookingEdit, name='booking_edit'),
    # REVIEWS
    path('profile/my_review_list', views.review_list, name='my_review_list'),
]
