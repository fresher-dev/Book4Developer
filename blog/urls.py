from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/<int:pk>/", views.your_posts, name="your_posts"),
    path("<int:pk>/", views.blog_explorer, name="post"),
    path("contact/", views.contact, name="contact"),
    path("single/<str:user>/", views.single, name="single"),
    path("<int:pk>/<slug:slug>/", views.detail, name="detail"),
    path("edit/<int:pid>/", views.post_edit, name="edit"),
    path("<int:pk>/delete", views.post_delete, name="delete"),
    path("search/", views.search_post, name="search"),
    path("tags/<str:name>/", views.view_tag, name="tag"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
