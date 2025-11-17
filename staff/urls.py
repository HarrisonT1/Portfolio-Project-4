from django.urls import path
from . import views

urlpatterns = [
    # BOOKINGS
    path('staff/dashboard/booking_list/', views.StaffBookingList, name='staff_booking_list'),
    path('staff/dashboard/booking_list/view/<str:booking_id>/', views.ViewBooking, name='view_booking'),
    # REVIEWS
    path('staff/dashboard/review_list/', views.StaffReviewList, name='staff_review_list'),
    path('staff/dashboard/review_list/view/<int:review_id>/', views.ViewReview, name='staff_review_view'),
]
