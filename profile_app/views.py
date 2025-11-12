from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Booking

# Create your views here.


def Profile(request):
    return HttpResponse("Hello, World!")


@login_required
def BookingList(request):
    bookings = Booking.objects.all().filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})