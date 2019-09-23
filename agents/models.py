from django.db import models

# Create your models here.
class Agent(models.Model):
	name_id = models.AutoField(primary_key=True)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email = models.EmailField(null=True)
	phone = models.CharField(max_length=11,null=True)
	pollingunit_uniqueid = models.IntegerField(null=True)

	class Meta:
		db_table = 'agentname'

	def __str__(self):
		return "%s %s" %(self.lastname, self.firstname)