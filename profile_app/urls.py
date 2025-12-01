from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    # GENERAL
    path(
        'profile/',
        views.profile,
        name='show_profile'),

    path(
        'profile/edit_profile/',
        views.edit_profile,
        name='edit_profile'),

    # BOOKINGS

    path(
        'profile/bookings/',
        views.booking_list,
        name='booking_list'),

    path(
        'profile/bookings/<str:booking_id>/',
        views.booking_details,
        name='booking_details'),

    path('profile/bookings/<str:booking_id>/cancel/',
         views.booking_cancel,
         name='booking_cancel'),

    path('profile/bookings/<str:booking_id>/edit/',
         views.booking_edit,
         name='booking_edit'),
    # REVIEWS
    path(
        'profile/my_review_list/',
        views.review_list,
        name='my_review_list'),

    path(
        'profile/my_review_list/<int:review_id>/cancel/',
        views.review_cancel,
        name='review_cancel'),

    path(
        'profile/my_review_list/<int:review_id>/edit/',
        views.review_edit,
        name='review_edit'),
]
