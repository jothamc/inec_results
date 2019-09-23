from django.urls import path
from results.views import PollingUnitResultView,PollingUnitListView

app_name = "pu"
urlpatterns = [
	path('',PollingUnitListView.as_view(),name="list"),
	path('<int:pu_id>/',PollingUnitResultView.as_view(),name="result"),
]