from django.urls import path
from . import views

urlpatterns = [
    # STAFF DASHBOARD
    path(
        'staff/dashboard/',
        views.staff_dashboard,
        name='staff_dashboard'),
    # BOOKINGS
    path(
        'staff/dashboard/booking_list/',
        views.staff_booking_list,
        name='staff_booking_list'),
    path(
        'staff/dashboard/booking_list/view/<str:booking_id>/',
        views.view_booking,
        name='view_booking'),
    path(
        'staff/dashboard/booking_list/approve/<str:booking_id>/',
        views.approve_booking,
        name='approve_booking'),
    path(
        'staff/dashboard/booking_list/deny/<str:booking_id>/',
        views.deny_booking,
        name='deny_booking'),
    # REVIEWS
    path(
        'staff/dashboard/review_list/',
        views.staff_review_list,
        name='staff_review_list'),

    path(
        'staff/dashboard/review_list/view/<int:review_id>/',
        views.view_review,
        name='staff_review_view'),

    path(
        'staff/dashboard/review_list/approve/<int:review_id>/',
        views.approve_review,
        name='approve_review'),

    path(
        'staff/dashboard/review_list/deny/<int:review_id>/',
        views.deny_review,
        name='deny_review'),
    # COMMENTS
    path(
        'staff/dashboard/comment_list/',
        views.comment_list,
        name='staff_comment_list'),
    path(
        'staff/dashboard/comment_list/<int:comment_id>/approve/',
        views.approve_comment,
        name='approve_comment'),
    path(
        'staff/dashboard/comment_list/<int:comment_id>/deny/',
        views.deny_comment,
        name='deny_comment'),
]
