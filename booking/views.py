from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import Booking

# Create your views here.


@login_required
def CreateBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return HttpResponseRedirect('/')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_template.html', {'form': form})


def BookingList(request):
    bookings = Booking.objects.all().filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})