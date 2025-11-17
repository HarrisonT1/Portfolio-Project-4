from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory

urlpatterns = [
    path('reviews/', views.review_list, name='review_list'),
    path('review/create/', views.CreateReview, name='create_review'),
    path('review/success/<int:review_id>/', views.ReviewSuccess, name='review_success'),
    path('review/<int:review_id>/', views.review_view, name='review_view'),
    path('review/<int:review_id>/comment/', views.create_comment, name='create_comment'),
]