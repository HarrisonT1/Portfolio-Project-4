from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star_rating', 'comment']
        widgets = {
            'star_rating': forms.Select(),
            'comment': forms.Textarea()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
