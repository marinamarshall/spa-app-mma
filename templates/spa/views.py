from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Treatment


class TreatmentList(generic.ListView):
    """ TreatmentList """
    model = Treatment
    queryset = Treatment.objects.all()
    template_name = 'index.html'

class TreatmentDetail(View):
    """ TreatmentDetail """
    def get(self, request, slug, *args, **kwargs):
        queryset = Treatment.objects.all()
        treatment = get_object_or_404(queryset, slug=slug)

        return render(
            request, 
            'treatment_detail.html',
            {
                "treatment":treatment
            },
        )