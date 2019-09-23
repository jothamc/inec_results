from django.urls import path
from results.views import LGAListView,LGAResultSumView
app_name = "lgas"
urlpatterns = [
	path('',LGAListView.as_view(),name="lga-list"),
	path('results/',LGAResultSumView.as_view(),name="lga-sum"),

]