from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=2020, null=True, blank=True)
	phone = models.CharField(max_length=11, null=True, blank=True)
	address = models.CharField(max_length=2022, blank=True, null=True)
	image = models.ImageField(upload_to="image", default="img/default.png")
	created_date = models.DateTimeField(default=timezone.now)

	website = models.URLField(null=True, blank=True)
	github = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	instagram = models.URLField(null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.user.username
