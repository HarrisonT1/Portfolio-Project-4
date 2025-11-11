from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm

# Create your views here.

def CreateBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_template.html', {'form': form})