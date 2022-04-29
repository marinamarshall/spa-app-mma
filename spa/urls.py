from django.urls import path
from . import views
from . import forms


urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home'),
    path('<slug:slug>/', views.TreatmentDetail.as_view(), name="treatment_detail"),
    # path('bookingform/', forms.BookingForm.as_view(), name="booking_form"),
]
