from django.shortcuts import render
from django.views import generic
from .models import Treatment


class TreatmentList(generic.ListView):
    """ TreatmentList """
    model = Treatment
    queryset = Treatment.objects.all()
    template_name = 'index.html'
