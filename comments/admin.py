from django.contrib import admin
from .models import BlogComment, BookComment


admin.site.register(BlogComment)
admin.site.register(BookComment)