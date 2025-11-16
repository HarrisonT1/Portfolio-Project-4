from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from booking.models import Booking

# Create your views here.


def StaffBookingList(request):
    bookings = Booking.objects.all()
    return render(request, 'staff/staff_booking_list.html', {'bookings': bookings})


def ApproveBooking(request, booking_id):
    booking = Booking.objects.filter(booking_id=booking_id, approved='pending').first()
    if not booking:
        messages.error(request, "Booking not found")
        return redirect('staff_booking_list')
    booking.approved = 'approved'
    booking.save()
    return redirect('staff_booking_list')


def DenyBooking(request, booking_id):
    booking = Booking.objects.filter(booking_id=booking_id, approved='pending').first()
    if not booking:
        messages.error(request, "Booking not found")
        return redirect('staff_booking_list')
    booking.approved = 'denied'
    booking.save()
    return redirect('staff_booking_list')
