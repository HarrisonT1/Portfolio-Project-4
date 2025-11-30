from django import forms
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '').strip()
        if first_name and not first_name.isalpha():
            raise forms.ValidationError(
                "Your first name must only contain letters")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '').strip()
        if last_name and not last_name.isalpha():
            raise forms.ValidationError(
                "Your last name must only contain letters")
        return last_name
