from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from books.models import Book


class BlogReview(models.Model):

	RATE_CHOICES = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5)
	)

	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	starts = models.IntegerField(choices=RATE_CHOICES)
	comment = models.TextField(null=True, blank=True)
	review_date = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)


	def __str__(self):
		return self.post.title



class BookRating(models.Model):

	RATE_STAR = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5)
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	rating = models.IntegerField(choices=RATE_STAR)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)


	def __str__(self):
		return "{} book => {} star rating.".format(self.book.title, self.rating)