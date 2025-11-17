from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from booking.models import Booking
from reviews.models import Review


# Create your views here.


# BOOKING

def StaffBookingList(request):
    bookings = Booking.objects.all()
    return render(request, 'staff/staff_booking_list.html', {'bookings': bookings})


def ApproveBooking(request, booking_id):
    booking = Booking.objects.filter(booking_id=booking_id, approved='pending').first()
    if not booking:
        messages.error(request, "Booking not found")
        return redirect('staff_booking_list')
    booking.approved = 'approved'
    booking.save()
    return redirect('staff_booking_list')


def DenyBooking(request, booking_id):
    booking = Booking.objects.filter(booking_id=booking_id, approved='pending').first()
    if not booking:
        messages.error(request, "Booking not found")
        return redirect('staff_booking_list')
    booking.approved = 'denied'
    booking.save()
    return redirect('staff_booking_list')


def ViewBooking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    return render(request, 'staff/staff_booking_view_booking.html', {'booking': booking})

# REVIEWS


def StaffReviewList(request):
    reviews = Review.objects.all()
    return render(request, 'staff/staff_review_list.html', {'reviews': reviews})


def ApproveReview(request, Review_id):
    review = Review.objects.filter(Review_id=Review_id, approved='pending').first()
    if not review:
        messages.error(request, "Review not found")
        return redirect('staff_review_list')
    review.approved = 'approved'
    review.save()
    return redirect('staff_review_list')



# def DenyReview
# def ViewReview
