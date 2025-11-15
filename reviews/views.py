
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm

# Create your views here.

@login_required
def CreateReview(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('create_review')
    else:
        form = ReviewForm()

    return render(request, "reviews/create_review.html", {"form": form})