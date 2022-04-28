from django.urls import path
from . import views


urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home'),
    path('<slug:slug>/', views.TreatmentDetail.as_view(), name="treatment_detail"),
]
