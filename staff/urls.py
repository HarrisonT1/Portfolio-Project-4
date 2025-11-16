from django.urls import path
from . import views

urlpatterns = [
    path('staff/dashboard/', views.StaffDashboard, name='staff_dashboard'),
    path('staff/dashboard/booking_list/approve/<int:booking_id>/', views.ApproveBooking, name='approve_booking'),
]
