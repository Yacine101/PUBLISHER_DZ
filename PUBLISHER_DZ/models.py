from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Post(models.Model):
#	author=models.ForeignKey('auth.User')
	description=models.TextField(max_length=500)
	location=models.CharField(max_length=50)
	phone=models.CharField(max_length=50)
	e_mail=models.CharField(max_length=50)
	creation_date=models.DateTimeField(default=timezone.now)
	image_url=models.CharField(max_length=100)
        keywords=models.CharField(max_length=100)

	def handle_post(self):
		self.creation_date=timezone.now()
		self.save
	
	def __str__(self):
		return self.description	

# Create your models here.
