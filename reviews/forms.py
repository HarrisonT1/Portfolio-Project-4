from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star_rating', 'comment']
        widgets = {
            'star_rating': forms.Select(),
            'comment': forms.Textarea()
        }
