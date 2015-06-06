from django.db import models

# Create your models here.
class Organization(models.Model):
	organization_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	contact_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=200)

	def __str__(self):
		return self.organization_name