from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review

# Create your views here.


@login_required
def CreateReview(request):
    user = request.user
    # Need to add profile editability **************
    if not user.first_name or not user.last_name:
        messages.error(request, "Please add a first and last name to your profile before continuing")
        next_url = reverse('create_review')
        edit_profile_url = f"{reverse('edit_profile')}?next={next_url}"
        return redirect(edit_profile_url)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_success', review_id=review.id)
    else:
        form = ReviewForm()

    return render(request, "reviews/create_review.html", {"form": form})


@login_required
def ReviewSuccess(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'reviews/review_success.html', {'review': review})


def review_list(request):
    reviews = Review.objects.filter(approved='approved').order_by('-star_rating')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


def review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id, approved='approved')
    comments = review.comments.all().order_by('-created_at')

    context = {
        'review': review,
        'comments': comments
    }

    return render(request, 'review/review_view.html', context)


def create_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id, approved='approved')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('create_comment', review_id=review.id)
    else:
        form = CommentForm()

    context = {
        'review': review,
        'form': form,
    }

    return render(request, 'review/create_comment.html', context)
