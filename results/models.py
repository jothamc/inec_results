from django.db import models
from polling_units.models import PollingUnit
from parties.models import Party
# Create your models here.




class PollingUnitResult(models.Model):
	result_id = models.AutoField(primary_key=True)
	polling_unit = models.ForeignKey(PollingUnit,on_delete=models.CASCADE,null=True,db_column='polling_unit_uniqueid')
	party = models.ForeignKey(Party,on_delete=models.CASCADE,db_column='party_abbreviation',null=True)
	party_score = models.IntegerField()
	entered_by_user = models.CharField(max_length=200)
	date_entered = models.DateField(auto_now_add=True)
	user_ip_address = models.GenericIPAddressField(null=True)


	class Meta:
		verbose_name = "Result"
		verbose_name_plural = "Results"
		db_table = 'announced_pu_results'


	def __str__(self):
		return "%s %d" %(self.polling_unit,self.result_id)

