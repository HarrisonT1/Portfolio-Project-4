from django.urls import path
from . import views

urlpatterns = [
    # STAFF DASHBOARD
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    # BOOKINGS
    path('staff/dashboard/booking_list/', views.StaffBookingList, name='staff_booking_list'),
    path('staff/dashboard/booking_list/view/<str:booking_id>/', views.ViewBooking, name='view_booking'),
    # REVIEWS
    path('staff/dashboard/review_list/', views.StaffReviewList, name='staff_review_list'),
    path('staff/dashboard/review_list/view/<int:review_id>/', views.ViewReview, name='staff_review_view'),
    # COMMENTS
    path('staff/dashboard/comment_list/', views.comment_list, name='staff_comment_list'),
    path('staff/dashboard/comment_list/<int:comment_id>/approve/', views.approve_comment, name='approve_comment'),
    path('staff/dashboard/comment_list/<int:comment_id>/deny/', views.deny_comment, name='deny_comment'),
]
