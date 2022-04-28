from . import views
from django.urls import path

urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home')
]