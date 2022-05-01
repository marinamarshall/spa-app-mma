from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Treatment, Booking
from .forms import BookingForm


class TreatmentList(generic.ListView):
    """ TreatmentList """
    model = Treatment
    queryset = Treatment.objects.all().order_by('category')
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


class BookingView(FormView):
    """ BookingView """
    template_name = 'book_treatment.html'
    form_class = BookingForm
    success_url = '/viewbookings/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.save()
        return super().form_valid(form)
    # if form.is_valid return render(request, 'view_bookings.html')
    # else booking_form = BookingForm()

# Your Treatments - View List


class BookingList(ListView):
    """ BookingList """
    template_name = 'view_bookings.html'
    queryset = Booking.objects.all()
    model = Booking

    # treatment = get_object_or_404(queryset)

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
