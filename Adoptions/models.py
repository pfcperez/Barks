from django.db import models

# Create your models here.
class Adoption(models.Model):
	adoption_date = models.DateField(auto_now=False)
	comments = models.CharField(max_length=100)