from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from booking.models import Booking

# Create your views here.


def ApproveBooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.aprroved = 'approved'
    booking.save()
    return redirect('staff_booking_list')
