from django import forms
from datetime import date, time, datetime
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'booking_date',
            'booking_time',
            'comments',
            'number_of_people',
        ]
        labels = {
            'number_of_people': 'Number of people (including yourself)'
        }

        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'booking_time': forms.TimeInput(
                attrs={
                    'type': 'time'
                },
                format='%H:%M'
            ),
        }

    def clean_number_of_people(self):
        number = self.cleaned_data.get('number_of_people')
        if number < 1:
            raise forms.ValidationError("Number of people must be at least 1")
        return number

    def clean_booking_date(self):
        input = self.cleaned_data["booking_date"]
        if input < date.today():
            raise forms.ValidationError("You can only select a future date")
        return input

    def clean_booking_time(self):
        input_time = self.cleaned_data["booking_time"]
        input_date = self.cleaned_data["booking_date"]
        now = datetime.now()

        if not (time(9, 0) <= input_time <= time(16, 0)):
            raise forms.ValidationError(
                "You can only select a time within hours 9am-4pm")

        if input_date == now.date() and input_time <= now.time():
            raise forms.ValidationError(
                "You cannot book in the past"
            )
        return input_time
