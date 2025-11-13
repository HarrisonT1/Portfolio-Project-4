from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Booking
from booking.forms import BookingForm

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


@login_required
def BookingEdit(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)

    form = BookingForm(request.POST or None, instance=booking)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            # Add code to reset approval from staff member once staff app is created

            messages.success(request, "Your booking has successfully been updated and is awaiting staff approval!")
            return redirect('booking_list')
        else:
            messages.error(request, "Error updating your booking. Please review your changes and try again.")

    context = {
        'form': form,
        'booking': booking
    }
    return render(request, 'profile_app/booking_edit.html', context)
