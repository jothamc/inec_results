from django.db import models
from lgas.models import LGA

# Create your models here.

class PollingUnit(models.Model):
	uniqueid = models.AutoField(primary_key=True)
	polling_unit_id = models.IntegerField()
	ward_id = models.IntegerField()
	lga = models.ForeignKey(LGA,on_delete=models.CASCADE,null=True)
	uniquewardid = models.IntegerField()
	polling_unit_number = models.IntegerField()
	polling_unit_name = models.CharField(max_length=200)
	polling_unit_description = models.TextField()
	lat = models.FloatField()
	long = models.FloatField()
	entered_by_user = models.CharField(max_length=200)
	date_entered = models.DateField(auto_now_add=True)
	user_ip_address = models.GenericIPAddressField(null=True)

	class Meta:
		db_table = "polling_unit"
