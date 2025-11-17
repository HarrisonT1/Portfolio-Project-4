
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Booking
from booking.forms import BookingForm
from reviews.models import Review
from .forms import EditProfileForm

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


@login_required
def profile(request):
    user = request.user
    bookings = user.bookings.all()
    reviews = user.reviews.all()

    context = {
        'bookings': bookings,
        'reviews': reviews,
    }

    return render(request, 'profile_app/profile_details.html', context)


@login_required
def EditProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            next_url = request.GET.get('next') or reverse('show_profile')
            return redirect(next_url)
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'profile_app/edit_profile.html', {'form': form})


@login_required
def review_list(request):
    user = request.user

    approved_reviews = Review.objects.filter(user=user, approved='approved').order_by('-created_at')
    awaiting_approval_reviews = Review.objects.filter(user=user, approved='pending').order_by('-created_at')

    context = {
        'approved_reviews': approved_reviews,
        'awaiting_approval_reviews': awaiting_approval_reviews,
    }

    return render(request, 'profile_app/my_review_list.html', context)
