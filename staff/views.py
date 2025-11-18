from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from datetime import date
from booking.models import Booking
from reviews.models import Review, Comment


# Create your views here.

# STAFF DASHBOARD

def staff_dashboard(request):
    total_bookings = Booking.objects.count()
    future_bookings = Booking.objects.filter(booking_date__gte=date.today()).count()
    pending_bookings = Booking.objects.filter(approved='pending').count()
    past_bookings = Booking.objects.filter(booking_date__lt=date.today()).count()
    total_reviews = Review.objects.count()
    pending_reviews = Review.objects.filter(approved='pending').count()
    total_users = User.objects.count()

    context = {
        'total_bookings': total_bookings,
        'future_bookings': future_bookings,
        'pending_bookings': pending_bookings,
        'past_bookings': past_bookings,
        'total_reviews': total_reviews,
        'pending_reviews': pending_reviews,
        'total_users': total_users,
    }

    return render(request, 'staff/staff_dashboard.html', context)


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
    return render(request, 'staff/staff_booking_view.html', {'booking': booking})

# REVIEWS


def StaffReviewList(request):
    reviews = Review.objects.all()
    return render(request, 'staff/staff_review_list.html', {'reviews': reviews})


def ApproveReview(request, review_id):
    review = Review.objects.filter(id=review_id).first()
    if not review:
        messages.error(request, "Review not found")
        return redirect('staff_review_list')
    review.approved = 'approved'
    review.save()
    return redirect('staff_review_list')


def DenyReview(request, review_id):
    review = Review.objects.filter(id=review_id).first()
    if not review:
        messages.error(request, "Review not found")
        return redirect('staff_review_list')
    review.approved = 'denied'
    review.save()
    return redirect('staff_review_list')


def ViewReview(request, review_id):
    review = Review.objects.filter(id=review_id).first()
    if not review:
        messages.error(request, "Review not found")
        return redirect('staff_review_list')
    return render(request, 'staff/staff_review_view.html', {'review': review})


# COMMENTS


def comment_list(request):
    comments = Comment.objects.all()
    approved_comments = Comment.objects.filter(approved='approved')
    pending_comments = Comment.objects.filter(approved='pending')
    denied_comments = Comment.objects.filter(approved='denied')

    context = {
        'comments': comments,
        'approved_comments': approved_comments,
        'pending_comments': pending_comments,
        'denied_comments': denied_comments,
    }

    return render(request, 'staff/staff_comment_list.html', context)


def approve_comment(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    if not comment:
        messages.error(request, "Comment not found")
        return redirect('staff_comment_list')
    comment.approved = 'approved'
    comment.save()
    return redirect('staff_comment_list')


def deny_comment(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    if not comment:
        messages.error(request, "Comment not found")
        return redirect('staff_comment_list')
    comment.approved = 'denied'
    comment.save()
    return redirect('staff_comment_list')
