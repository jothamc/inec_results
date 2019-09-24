from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import PollingUnitResult
from polling_units.models import PollingUnit
from lgas.models import LGA
from parties.models import Party
from collections import Counter
from django import forms

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



class PollingUnitResultCreateView(CreateView):
	model = PollingUnitResult
	template_name = "pu_result_create.html"
	context_object_name = "results"
	fields = '__all__'

class ResultForm(forms.ModelForm):
	class Meta:
		model = PollingUnitResult
		fields = "__all__"




def PR(request):
	parties = Party.objects.all()
	if request.method == "GET":
		form = ResultForm()
	elif request.method == "POST":
		for r in request.POST:
			if len(r)==1:
				pu=PollingUnit.objects.get(polling_unit_name='new_pu')
				party = Party.objects.get(id=r)
				score = int(request.POST[r]) or 0
				user = request.POST['entered_by_user']
				result = PollingUnitResult(entered_by_user=user,party=party,
					polling_unit=pu,party_score=score,user_ip_address="127.0.0.1")
				result.save()


		# PollingUnitResult()
		form = ResultForm(request.POST)
	return render(request,"pu_result_create.html",{"form":form,"parties":parties})



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