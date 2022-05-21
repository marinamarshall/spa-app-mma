from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import reverse
from .models import Treatment, Booking
from .forms import BookingForm, EditForm


# TREATMENT VIEWS
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
                # "booking_form": BookingForm(),
                "booked": False
            },
        )


# BOOKING VIEWS
# Displays the Booking Form to Book a Treatment
class BookingView(CreateView):
    """ BookingView """
    model = Booking
    template_name = 'book_treatment.html'
    fields = ('client', 'treatment', 'date_of_treatment', 'time_of_treatment')
    # form_class = BookingForm
    success_url = '/viewbookings/'

    # def form_valid(self, form):
    #     form.instance.client = self.request.user
    #     form.save()
    #     return super().form_valid(form)


# CURRENT BOOKING VIEWS
# Your Treatments - View List
class BookingList(DetailView):
    """ BookingList """
    model = Booking
    template_name = 'view_bookings.html'

    def get(self, request, *args, **kwargs):
        """ filter """
        queryset = Booking.objects.filter(client=self.request.user, status=1)
        return render(
            request,
            'view_bookings.html',
            {
                "booking": queryset,
            },
        )


# To Edit a Booking
class EditBookings(UpdateView):
    """ EditBookings """
    model = Booking
    template_name = 'edit_bookings.html'
    # form_class = EditForm
    fields = ('client', 'treatment', 'date_of_treatment', 'time_of_treatment')
    success_url = '/viewbookings/'

    # def edit_your_booking(self):
    #     return reverse('edit_bookings')

    # def form_valid(self, form):
    #     """ form_valid """
    #     form.instance.client = self.request.user
    #     form.save()
    #     return super().form_valid(form)

