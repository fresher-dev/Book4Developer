from django.db import models
from blog.models import Post
from django.contrib.auth.models import User
from books.models import Book



class BlogComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        self.name = ''
        if self.user is None:
            self.name = "AnonymousUser"
        else:
            self.name = self.user
        return "Comment := {} <==> {} ".format(self.name, self.post.title)



class BookComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)


    def __str__(self):
        self.name = ''
        
        if self.user is None:
            self.name = "AnonymousUser"
        else:
            self.name = self.user


        return "Comment := {} <==> {} ".format(self.name, self.book.title)
