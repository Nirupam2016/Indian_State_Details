from django.db import models

# Create your models here.

class State(models.Model):
	name=models.CharField(max_length=100)
	capital=models.CharField(max_length=100)
	chief_minister=models.CharField(max_length=100)
	governor=models.CharField(max_length=100)

	def __str__(self):
		return self.name
