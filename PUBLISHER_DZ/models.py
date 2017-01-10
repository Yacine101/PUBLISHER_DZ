from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Post(models.Model):
	author=models.ForeignKey('auth.User')
	description=models.CharField(max_length=150)
	location=models.CharField(max_length=20)
	creation_date=models.DateTimeField(default=timezone.now)
	image_url=models.CharField(max_length=100)
        keyworks=models.CharField(max_length=100)

	def handle_post(self):
		self.creation_date=timezone.now()
		self.save
	
	def __str__(self):
		return self.description	

# Create your models here.
