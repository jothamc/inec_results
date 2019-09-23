from django.db import models
from agents.models import Agent
from polling_units.models import PollingUnit
# Create your models here.

class PollingUnitResult(models.Model):
	result_id = models.AutoField(primary_key=True)
	polling_unit = models.ForeignKey(PollingUnit,on_delete=models.CASCADE,null=True,db_column='polling_unit_uniqueid')
	party_abbreviation = models.CharField(max_length=10)
	party_score = models.IntegerField()
	entered_by_user = models.CharField(max_length=200)
	date_entered = models.DateField(auto_now_add=True)
	user_ip_address = models.GenericIPAddressField(null=True)


	class Meta:
		verbose_name = "Result"
		verbose_name_plural = "Results"
		db_table = 'announced_pu_results'


	def __str__(self):
		return "%d" %self.result_id

