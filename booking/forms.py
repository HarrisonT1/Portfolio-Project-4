from django import forms
from .models import Booking, Menu, Order


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'booking_date',
            'booking_time',
            'duration',
            'comments',
            'number_of_people',
        ]

        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'booking_time': forms.TimeInput(attrs={
                'type': 'time'
            })
        }


class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Order
        fields = ['items']
