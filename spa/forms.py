from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """ BookingForm """
    class Meta:
        """ Meta """
        model = Booking
        fields = ('treatment', 'date_of_treatment', 'time_of_treatment',)
