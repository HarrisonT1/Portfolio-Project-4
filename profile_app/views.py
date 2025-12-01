from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from booking.models import Booking
from booking.forms import BookingForm
from reviews.forms import ReviewForm
from reviews.models import Review
from .forms import EditProfileForm

# Create your views here.


@login_required
def booking_list(request):
    now = timezone.now()
    bookings = Booking.objects.all().filter(
        user=request.user, booking_date__gte=now.date())
    return render(
        request, 'profile_app/booking_list.html', {'bookings': bookings})


@login_required
def booking_details(request, booking_id):
    booking = get_object_or_404(
        Booking, booking_id=booking_id, user=request.user)
    return render(
        request, 'profile_app/booking_details.html', {'booking': booking})


@login_required
def booking_cancel(request, booking_id):
    booking = get_object_or_404(
        Booking, booking_id=booking_id, user=request.user)
    booking.delete()
    messages.warning(request, "Your booking has been cancelled")
    return redirect('booking_list')


@login_required
def booking_edit(request, booking_id):
    booking = get_object_or_404(
        Booking, booking_id=booking_id, user=request.user)

    form = BookingForm(request.POST or None, instance=booking)

    if request.method == 'POST':
        if form.is_valid():
            updated_booking = form.save(commit=False)
            updated_booking.approved = 'pending'
            updated_booking.save()
            messages.success(
                request,
                "Your booking has successfully been updated "
                "and is awaiting staff approval!")
            return redirect('booking_list')
        else:
            messages.error(
                request,
                "Error updating your booking. "
                "Please review your changes and try again.")

    context = {
        'form': form,
        'booking': booking
    }
    return render(request, 'profile_app/booking_edit.html', context)


@login_required
def profile(request):
    user = request.user
    bookings = user.bookings.all().count()
    reviews = user.reviews.all().count()
    comments = user.comment_set.all().count()

    context = {
        'bookings': bookings,
        'reviews': reviews,
        'comments': comments,
    }

    return render(request, 'profile_app/profile_details.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            next_url = request.GET.get('next') or reverse('show_profile')
            messages.success(
                request,
                "Your profile has successfully been updated")
            return redirect(next_url)
        else:
            messages.error(request, "Your profile could not be updated")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'profile_app/edit_profile.html', {'form': form})


@login_required
def review_list(request):
    user = request.user

    approved_reviews = Review.objects.filter(
        user=user, approved='approved').order_by('-created_at')
    awaiting_approval_reviews = Review.objects.filter(
        user=user, approved='pending').order_by('-created_at')

    context = {
        'approved_reviews': approved_reviews,
        'awaiting_approval_reviews': awaiting_approval_reviews,
    }

    return render(request, 'profile_app/my_review_list.html', context)


@login_required
def review_cancel(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    messages.warning(request, "Your Review has been cancelled")
    review.delete()
    return redirect('my_review_list')


@login_required
def review_edit(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    form = ReviewForm(request.POST or None, instance=review)

    if request.method == 'POST':
        if form.is_valid():
            update_review = form.save(commit=False)
            update_review.approved = 'pending'
            update_review.save()
            messages.success(
                request,
                "Your review has been updated,"
                " staff will check it for approval")
            return redirect('my_review_list')

    context = {
        'form': form,
        'review': review
    }

    return render(request, 'profile_app/review_edit.html', context)
