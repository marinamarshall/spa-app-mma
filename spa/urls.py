from django.urls import path
from . import views
# from . import forms


urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home'),
    path('bookingview/', views.BookingView.as_view(), name="booking_view"),
    path('viewbookings/', views.BookingList.as_view(), name="view_bookings"),
    path('editbookings/', views.EditBookings.as_view(), name="edit_bookings"),
    path('deletebookings/', views.DeleteBookings.as_view(), name="delete_bookings"),

    # a slug path need to be last
    path('<slug:slug>/', views.TreatmentDetail.as_view(), name="treatment_detail"),
]
