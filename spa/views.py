from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Treatment, Booking
from .forms import BookingForm, EditForm, DeleteForm


# Displays the Treatments on the home page - index.html
class TreatmentList(generic.ListView):
    """ TreatmentList """
    model = Treatment
    queryset = Treatment.objects.all().order_by('category')
    template_name = 'index.html'


# Displays the Treatment Detail after clicking the Treatment Details button - treatment_detail.html
class TreatmentDetail(View):
    """ TreatmentDetail """
    def get(self, request, slug, *args, **kwargs):
        """ get """
        queryset = Treatment.objects.all()
        treatment = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'treatment_detail.html',
            {
                "treatment": treatment,
                "booking_form": BookingForm(),
                "booked": False
            },
        )

# Displays the Booking Form to Book a Treatment
class BookingView(FormView):
    """ BookingView """
    template_name = 'book_treatment.html'
    form_class = BookingForm
    success_url = '/viewbookings/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.save()
        return super().form_valid(form)


# Your Treatments - View List
class BookingList(ListView):
    """ BookingList """
    template_name = 'view_bookings.html'
    queryset = Booking.objects.filter(status=1)
    model = Booking

    def get(self, request, *args, **kwargs):
        """ filter """
        queryset = Booking.objects.filter(status=1)
        return render(
            request,
            'view_bookings.html',
            {
                "booking": queryset,
                # "booked": True
            },
        )


# To Edit a Booking
class EditBookings(FormView):
    """ EditBookings """
    template_name = 'edit_bookings.html'
    form_class = EditForm
    success_url = '/viewbookings'

    def form_valid(self, form):
        """ form_valid """
        form.instance.client = self.request.user
        form.save()
        return super().form_valid(form)


class DeleteBookings(FormView):
    """ EditBookings """
    template_name = 'edit_bookings.html'
    form_class = DeleteForm
    success_url = '/viewbookings'

    def form_valid(self, form):
        """ form_valid """
        form.instance.client = self.request.user
        form.save()
        return super().form_valid(form)
