from django.urls import path
from . import views

urlpatterns = [
    path('staff/dashboard/booking_list/', views.StaffBookingList, name='staff_booking_list'),
    path('staff/dashboard/booking_list/approve/<str:booking_id>/', views.ApproveBooking, name='approve_booking'),
]
