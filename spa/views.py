from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from .models import Treatment, Booking
from .forms import BookingForm


class TreatmentList(generic.ListView):
    """ TreatmentList """
    model = Treatment
    queryset = Treatment.objects.all()
    template_name = 'index.html'


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

    def post(self, request, slug, *args, **kwargs):
        """ post """
        queryset = Treatment.objects.all()
        treatment = get_object_or_404(queryset, slug=slug)

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.instance.treatment = request.client.treatment
            booking_form.instance.date_of_treatment = request.client.date_of_treatment
            booking_form.instance.time_of_treatment = request.client.time_of_treatment
            booking = booking_form.save(commit=False)
            booking.post = booking
            booking.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            'treatment_detail.html',
            {
                "treatment": treatment,
                "booking_form": BookingForm(),
                "booked": True
            },
        )


# Book Your Treatment - form
# add post method? generic View
class BookingView(CreateView):
    """ BookingView """
    template_name = 'book_treatment.html'
    form_class = BookingForm
    # model = Booking
    # queryset = Booking.objects.all()

    # Maybe make this a post method as it is to submit a request for a booking
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    # if form.is_valid return render(request, 'view_bookings.html')
    # else booking_form = BookingForm()


# Your Treatments - View List
# add get method? generic View
class BookingList(ListView):
    """ BookingList """
    template_name = 'view_bookings.html'
    queryset = Booking.objects.all()
    model = Booking

    treatment = get_object_or_404(queryset)

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'view_bookings.html',
            {
                # "treatment": treatment,
                # "booking_form": BookingForm(),
                # "booked": True
            },
        )
