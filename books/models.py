from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tags.models import Tag

class Book(models.Model):
	"""docstring for Book"""
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	slug = models.SlugField()
	pdf_file = models.FileField(upload_to="file", null=True, blank=True)
	cover = models.ImageField(upload_to="bookimage", default="img/book.png")
	link = models.CharField(max_length=2082, blank=True, null=True)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	created_date = models.DateTimeField(default=timezone.now)
	edited_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title
