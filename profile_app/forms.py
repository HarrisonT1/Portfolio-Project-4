from django import forms
from django.contrib.auth.models import User


class EditProfile(forms.ModelForm):
    class meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
