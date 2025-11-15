from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review

# Create your views here.

@login_required
def CreateReview(request):
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