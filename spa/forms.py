from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """ BookingForm """
    class Meta:
        """ Meta """
        model = Booking
        fields = ('treatment', 'date_of_treatment', 'time_of_treatment',)


class EditForm(forms.Form):
    """ EditForm """
    class Meta:
        """ Meta """
        # model = Booking
        name = forms.CharField(label='Your name')
        comment = forms.Textarea()
        # fields = ('treatment', 'date_of_treatment', 'time_of_treatment',)
