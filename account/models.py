from django.db import models
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
	"""docstring for Profile"""
	username = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=200)
	slug = models.SlugField()
	description = models.CharField(max_length=2020, null=True, blank=True)
	phone = models.CharField(max_length=11, null=True, blank=True)
	address = models.CharField(max_length=2022, blank=True, null=True)
	image = models.ImageField(upload_to="image", default="../static/default.png")


	def __str__(self):
		return self.username



		