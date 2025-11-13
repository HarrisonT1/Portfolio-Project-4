from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Booking

# Create your views here.


@login_required
def BookingList(request):
    bookings = Booking.objects.all().filter(user=request.user)
    return render(request, 'profile_app/booking_list.html', {'bookings': bookings})


@login_required
def BookingDetails(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    return render(request, 'profile_app/booking_details.html', {'booking': booking})


@login_required
def BookingCancel(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    booking.delete()
    return redirect('booking_list')
