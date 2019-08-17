from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	registration_no= models.CharField(max_length=200)
	rc=models.ImageField(default='default.bmp',upload_to='rc_images/')
	insurance=models.ImageField(default='default.bmp',upload_to='insurance_images/')
	pollution=models.ImageField(default='default.bmp',upload_to="pollution_images/")
	extra=models.TextField(default='none')

	def __str__(self):
		return self.registration_no
