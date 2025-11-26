from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, OrderForm, OrderItemFormSet
from .models import Booking, Order, Menu

# Create your views here.


@login_required
def CreateBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            messages.success(request, "Your booking was success, see your bookings for details.")

            return redirect('booking_success', booking_id=booking.booking_id)
        else:
            messages.error(request, "Your booking has failed. Please try again.")
    else:
        form = BookingForm()
    return render(request, 'booking/booking_template.html', {'form': form})


@login_required
def BookingSuccess(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    return render(request, 'booking/booking_success.html', {'booking': booking})


@login_required
def food_order(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    order, created = Order.objects.get_or_create(booking=booking)

    if request.method == 'POST':
        formset = OrderItemFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('booking_success')
    else:
        formset = OrderItemFormSet(instance=order)

    context = {
        'booking': booking,
        'formset': formset,
    }

    return render(request, 'booking/create_order.html', context)
