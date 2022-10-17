from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path("", views.home, name="home"),
	path("login/", views.singin, name="login"),
	path("register/", views.singup, name="register"),
	path("logout/", views.singout, name="logout"),
	path("<int:pk>/", views.profile_page, name="profile"),
	path("<int:pk>/edit/", views.edit_page, name="edit"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)