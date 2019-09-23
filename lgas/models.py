from django.db import models

# Create your models here.



class LGA(models.Model):
	uniqueid = models.AutoField(primary_key=True)
	lga_id = models.IntegerField()
	lga_name = models.CharField(max_length=100)
	lga_description = models.TextField()
	state_id = models.IntegerField()
	entered_by_user = models.CharField(max_length=200)
	date_entered = models.DateField(auto_now_add=True)
	user_ip_address = models.GenericIPAddressField(null=True)

	class Meta:
		db_table = "lga"
		verbose_name='LGA'
		verbose_name_plural = 'LGAs'


