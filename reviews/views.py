from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import ReviewForm, CommentForm
from .models import Review

# Create your views here.


@login_required
def create_review(request):
    user = request.user
    if not user.first_name or not user.last_name:
        if not messages.get_messages(request):
            messages.error(
                request,
                "Please add a first and last name to your "
                "profile before continuing")
        next_url = reverse('create_review')
        edit_profile_url = f"{reverse('edit_profile')}?next={next_url}"
        return redirect(edit_profile_url)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Your review was a successs!")
            return redirect('review_success', review_id=review.id)
        else:
            messages.error(request, "Your review has failed, please try again")
    else:
        form = ReviewForm()

    return render(request, "reviews/create_review.html", {"form": form})


@login_required
def review_success(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'reviews/review_success.html', {'review': review})


def review_list(request):
    reviews = Review.objects.filter(
        approved='approved').order_by('-star_rating')

    paginator = Paginator(reviews, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'reviews/review_list.html', {'page_obj': page_obj})


@login_required
def review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    comments = review.comments.filter(
        approved="approved").order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.approved = 'pending'
            comment.save()
            messages.success(
                request,
                "Your comment has been made and is waiting"
                " approval from staff.")
            return redirect('review_view', review_id=review.id)
    else:
        form = CommentForm()

    context = {
        'review': review,
        'comments': comments,
        'form': form,
    }

    return render(request, 'profile_app/review_view.html', context)
