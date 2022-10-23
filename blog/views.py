from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Post
from tags.models import Tag
from django.contrib.auth.models import User
from .forms import PostForm
from comments.forms import CommentForm
from django.db.models import Q
from django.http import HttpResponse
from reviews.models import BlogReview
from reviews.forms import ReviewForm
from django.urls import reverse


def popular():
    top_post = Post.objects.all().order_by("-created_date")[:5]
    return top_post


def item_count():
    tag = Tag.objects.all()

    tags = {}

    for j in tag:
        tag_id = j.id
        tags[j] = Tag.objects.get(id=tag_id).post_set.all().count()

    return tags


def home(request):
    post = Post.objects.filter(status=1).order_by('-created_date')

    context = {
        "top_post": popular(),
        'tags': item_count(),
        "posts": post,
    }
    return render(request, "blog/home.html", context)


def your_posts(request, pk):
    user = User.objects.get(id=pk)

    post = Post.objects.filter(author=user).order_by('-created_date')
    draft = post.filter(status=1)

    context = {
        'posts': post,
        "top_post": popular(),
        'tags': item_count(),
        'drafts': draft,
    }
    return render(request, "blog/yourpost.html", context)


def detail(request, pk, slug):
    post = Post.objects.get(id=pk)
    if post.slug == slug:
        pass

    comment = post.blogcomment_set.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        "top_post": popular(),
        'tags': item_count(),
        "comment": comment,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }

    return render(request, 'blog/detail.html', context)


def blog_explorer(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.filter(author=user)
    draft = posts.filter(status=0)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            author = user
            slug = slugify(title)
            body = form.cleaned_data['body']
            tags = form.cleaned_data['tag']
            image = form.cleaned_data['image']
            status = form.cleaned_data['status']

            post = Post.objects.create(title=title.title(), author=author, slug=slug, body=body, image=image,
                                       status=status)

            for i in tags:
                post.tag.add(i)
                post.save()
            return redirect("blog:home")
    else:
        form = PostForm()

    context = {
        "form": form,
        "drafts": draft,
    }

    return render(request, 'blog/explorer.html', context)


def contact(request):
    return render(request, 'blog/contact.html')


def single(request, user):
    user = User.objects.get(username=user)

    context = {
        "top_post": popular(),
        'tags': item_count(),
        'users': user,

    }

    return render(request, 'blog/single.html', context)


def post_edit(request, pid):
    post = Post.objects.get(id=pid)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("blog:home")
    else:
        form = PostForm(instance=post)

    context = {
        "form": form
    }

    return render(request, 'blog/explorer.html', context)


def post_delete(request, pk):
    post = Post.objects.get(id=pk)

    post.delete()

    return redirect("blog:home")


def search_post(request):
    if request.method == "GET":
        queryset = request.GET.get('q')

        if queryset is not None:
            result = Post.objects.filter(Q(title__icontains=queryset))

    context = {
        "result": result,
    }

    return render(request, 'blog/search.html', context)


def view_tag(request, name):
    tag = Tag.objects.get(name=name)
    data = tag.post_set.all()

    context = {
        "data": data,
        "top_post": popular(),
        "tag": tag,
    }
    return render(request, "blog/tag.html", context)


def reviews(request, pk):
    post = Post.objects.get(id=pk)

    user = request.user

    if request.method == "POST":
        form = ReviewForm(request.POST or None)

        if form.is_valid():
            starts = form.cleaned_data['starts']
            comment = form.cleaned_data['comment']

            review = BlogReview.objects.create(starts=starts, comment=comment, post=post)
            review.save()
            return redirect(reverse("blog:detail", args=[post.id, post.slug]))

    else:
        form = ReviewForm()
        review = BlogReview.objects.filter(post=post)

    context = {
        "form": form,
        "review": review
    }

    return render(request, "reviews/review.html", context)