from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "books"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/<slug:slug>/", views.book_detail, name="book_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
