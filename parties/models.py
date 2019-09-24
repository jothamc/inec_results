from django.db import models

# Create your models here.


class Party(models.Model):
	id = models.AutoField(primary_key=True)
	partyid = models.CharField(max_length=10)
	partyname = models.CharField(max_length=10)

	class Meta:
		db_table = "party"

	def __str__(self):
		return self.partyname