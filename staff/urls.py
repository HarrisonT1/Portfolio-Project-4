from django.urls import path
from . import views

urlpatterns = [
    # STAFF DASHBOARD
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    # BOOKINGS
    path('staff/dashboard/booking_list/', views.StaffBookingList, name='staff_booking_list'),
    path('staff/dashboard/booking_list/view/<str:booking_id>/', views.ViewBooking, name='view_booking'),
    path('staff/dashboard/booking_list/approve/<str:booking_id>/', views.ApproveBooking, name='approve_booking'),
    path('staff/dashboard/booking_list/deny/<str:booking_id>/', views.DenyBooking, name='deny_booking'),
    # REVIEWS
    path('staff/dashboard/review_list/', views.StaffReviewList, name='staff_review_list'),
    path('staff/dashboard/review_list/view/<int:review_id>/', views.ViewReview, name='staff_review_view'),
    path('staff/dashboard/review_list/approve/<int:review_id>/', views.ApproveReview, name='approve_review'),
    path('staff/dashboard/review_list/deny/<int:review_id>/', views.DenyReview, name='deny_review'),
    # COMMENTS
    path('staff/dashboard/comment_list/', views.comment_list, name='staff_comment_list'),
    path('staff/dashboard/comment_list/<int:comment_id>/approve/', views.approve_comment, name='approve_comment'),
    path('staff/dashboard/comment_list/<int:comment_id>/deny/', views.deny_comment, name='deny_comment'),
]
