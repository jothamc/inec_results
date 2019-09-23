from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import PollingUnitResult
from polling_units.models import PollingUnit
from lgas.models import LGA
from collections import Counter

# Create your views here.


class LGAListView(ListView):
	model = LGA
	template_name = "lga-list.html"
	context_object_name = "results"




class PollingUnitListView(ListView):
	model = PollingUnit
	template_name = "lga_pu_list.html"
	context_object_name = "results"




class PollingUnitResultView(ListView):
	model = PollingUnitResult
	template_name = "pu_result_detail.html"
	context_object_name = "results"
	def get_queryset(self):
		pu_id = self.kwargs.get('pu_id')
		queryset = PollingUnitResult.objects.filter(polling_unit__uniqueid=pu_id)
		return queryset





class LGAResultSumView(ListView):
	model = PollingUnitResult
	template_name = "lga_sum.html"
	context_object_name = 'results'

	def get_queryset(self):
		lga_id = self.request.GET['lga-id']
		queryset = PollingUnitResult.objects.filter(polling_unit__lga__lga_id=lga_id)
		return queryset

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    queryset = self.get_queryset()
	    scores = {}
	    for result in queryset:
	    	if result.party_abbreviation in scores:
	    		scores[result.party_abbreviation]+=result.party_score
	    	else:
	    		scores[result.party_abbreviation]=result.party_score
	    	context['scores'] = scores
	    return context