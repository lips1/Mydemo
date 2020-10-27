from django.db import models




class signin(models.Model):

	username = models.CharField(max_length=100, null=True)
	password = models.CharField(max_length=100, null=True)
