from django.shortcuts import render
from .models import Book
from comments.forms import BookCommentForm


def home(request):
    books = Book.objects.all().order_by("-created_date")[:10]

    context = {
        "books": books
    }

    return render(request, "books/home.html", context)


def book_detail(request, slug, pk):
    book = Book.objects.get(id=pk)
    if slug == book.slug:
        pass

    comment = book.bookcomment_set.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = BookCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                new_comment.user = request.user
            new_comment.book = book
            new_comment.save()
    else:
        comment_form = BookCommentForm()

    context = {
        "book": book,
        "comment": comment,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }

    return render(request, "books/book_detail.html", context)
