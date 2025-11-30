from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from booking.models import Booking
from reviews.models import Review, Comment


# Create your views here.

# Staff access

def staff_access(view_func):
    is_staff_member = login_required(user_passes_test(lambda u: u.is_staff)(view_func))
    return is_staff_member

# STAFF DASHBOARD


@staff_access
def staff_dashboard(request):
    total_bookings = Booking.objects.count()
    future_bookings = Booking.objects.filter(booking_date__gte=date.today()).count()
    pending_bookings = Booking.objects.filter(approved='pending').count()
    past_bookings = Booking.objects.filter(booking_date__lt=date.today()).count()
    total_reviews = Review.objects.count()
    pending_reviews = Review.objects.filter(approved='pending').count()
    total_users = User.objects.count()
    total_comments = Comment.objects.filter(approved='approved').count()

    context = {
        'total_bookings': total_bookings,
        'future_bookings': future_bookings,
        'pending_bookings': pending_bookings,
        'past_bookings': past_bookings,
        'total_reviews': total_reviews,
        'pending_reviews': pending_reviews,
        'total_users': total_users,
        'total_comments': total_comments,
    }

    return render(request, 'staff/staff_dashboard.html', context)


# BOOKING


@staff_access
def StaffBookingList(request):
    bookings = Booking.objects.all().order_by("-booking_date")
    approved_bookings = Booking.objects.filter(approved='approved').order_by("-booking_date")
    pending_bookings = Booking.objects.filter(approved='pending').order_by("-booking_date")
    denied_bookings = Booking.objects.filter(approved='denied').order_by("-booking_date")

    context = {
        'bookings': bookings,
        'approved_bookings': approved_bookings,
        'pending_bookings': pending_bookings,
        'denied_bookings': denied_bookings,
    }

    return render(request, 'staff/staff_booking_list.html', context)


@staff_access
def ApproveBooking(request, booking_id):
    booking = Booking.objects.filter(booking_id=booking_id).first()
    if not booking:
        messages.error(request, "Booking not found")
        return redirect('staff_booking_list')
    booking.approved = 'approved'
    booking.save()
    messages.success(request, "Booking accepted")
    return redirect('staff_booking_list')


@staff_access
def DenyBooking(request, booking_id):
    booking = Booking.objects.filter(booking_id=booking_id).first()
    if not booking:
        messages.error(request, "Booking not found")
        return redirect('staff_booking_list')
    booking.approved = 'denied'
    booking.save()
    messages.error(request, "Booking denied")
    return redirect('staff_booking_list')


@staff_access
def ViewBooking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    return render(request, 'staff/staff_booking_view.html', {'booking': booking})

# REVIEWS


@staff_access
def StaffReviewList(request):
    reviews = Review.objects.all()
    approved_reviews = Review.objects.filter(approved='approved')
    pending_reviews = Review.objects.filter(approved='pending')
    denied_reviews = Review.objects.filter(approved='denied')

    context = {
        'reviews': reviews,
        'approved_reviews': approved_reviews,
        'pending_reviews': pending_reviews,
        'denied_reviews': denied_reviews,
    }

    return render(request, 'staff/staff_review_list.html', context)


@staff_access
def ApproveReview(request, review_id):
    review = Review.objects.filter(id=review_id).first()
    if not review:
        messages.error(request, "Review not found")
        return redirect('staff_review_list')
    review.approved = 'approved'
    review.save()
    messages.success(request, "Review accepted")
    return redirect('staff_review_list')


@staff_access
def DenyReview(request, review_id):
    review = Review.objects.filter(id=review_id).first()
    if not review:
        messages.error(request, "Review not found")
        return redirect('staff_review_list')
    review.approved = 'denied'
    review.save()
    messages.error(request, "Review denied")
    return redirect('staff_review_list')


@staff_access
def ViewReview(request, review_id):
    review = Review.objects.filter(id=review_id).first()
    if not review:
        messages.error(request, "Review not found")
        return redirect('staff_review_list')
    return render(request, 'staff/staff_review_view.html', {'review': review})


# COMMENTS


@staff_access
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


@staff_access
def approve_comment(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    if not comment:
        messages.error(request, "Comment not found")
        return redirect('staff_comment_list')
    comment.approved = 'approved'
    comment.save()
    messages.success(request, "Comment accepted")
    return redirect('staff_comment_list')


@staff_access
def deny_comment(request, comment_id):
    comment = Comment.objects.filter(id=comment_id).first()
    if not comment:
        messages.error(request, "Comment not found")
        return redirect('staff_comment_list')
    comment.approved = 'denied'
    comment.save()
    messages.error(request, "Comment denied")
    return redirect('staff_comment_list')
