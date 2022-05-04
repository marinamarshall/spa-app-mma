from django import forms
from .models import Booking, Update


class BookingForm(forms.ModelForm):
    """ BookingForm """
    class Meta:
        """ Meta """
        model = Booking
        fields = ('treatment', 'date_of_treatment', 'time_of_treatment',)


class EditForm(forms.ModelForm):
    """ EditForm """
    model = Update
    fields = ('name', 'new_specification',)
