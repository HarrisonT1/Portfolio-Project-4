from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking

# Create your views here.


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            messages.success(
                request,
                "Your booking was success, see your bookings for details.")

            return redirect('booking_success', booking_id=booking.booking_id)
        else:
            messages.error(
                request, "Your booking has failed. Please try again.")
    else:
        form = BookingForm()
    return render(request, 'booking/booking_template.html', {'form': form})


@login_required
def booking_success(request, booking_id):
    booking = get_object_or_404(
        Booking, booking_id=booking_id, user=request.user)
    return render(
        request, 'booking/booking_success.html', {'booking': booking})
