from django.urls import path
from . import views
from . import forms


urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home'),
    path('<slug:slug>/', views.TreatmentDetail.as_view(), name="treatment_detail"),
    # Should this path be to the html file book_treatment.html?
    # How to link form to html file?
    path('formforbooking/', forms.BookingForm, name="form_for_booking"),
    path('bookinglist/', forms.BookingForm, name="booking_list"),
]
