from django.forms import inlineformset_factory
from django import forms
from .models import Booking, Menu, Order, OrderItem


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

    def clean_number_of_people(self):
        number = self.cleaned_data.get('number_of_people')
        if number < 1:
            raise forms.ValidationError("Number of people must be at least 1")
        return number


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']


# Inspiried by stackoverflow post
OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    form=OrderForm,
    extra=5,
    can_delete=True,
)
