from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Post(models.Model):
	author=models.ForeignKey('auth.User')
	description=models.CharField(max_length="150")
	location=models.CharField(max_length="20")
	creation_date=models.DateTimeField(default=timezone.now)
	image_url=models.CharField(max_length="100")

	def publish(self):
		self.creation_date=timezone.now()
		self.save
	

# Create your models here.
