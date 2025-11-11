from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.

def CreateBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_template.html', {'form': form})