from django.db import models

# Create your models here.
class Friend(models.Model):
	friend_name = models.CharField(max_length=50)
	
	comments = models.CharField(max_length=100)

	def __str__(self):
		return self.friend_name