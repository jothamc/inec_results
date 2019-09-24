from django.urls import path
from results.views import PollingUnitResultView,PollingUnitListView,PollingUnitResultCreateView,PR

app_name = "pu"
urlpatterns = [
	path('',PollingUnitListView.as_view(),name="list"),
	path('<int:pu_id>/',PollingUnitResultView.as_view(),name="result"),
	# path('create/',PollingUnitResultCreateView.as_view(),name="create-result"),
	path('create/',PR,name="create-result"),
]