from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path("", views.home, name="home"),
	path("login/", views.singin, name="login"),
	path("register/", views.singup, name="register"),
	path("logout/", views.singout, name="logout"),
	path("<str:usr>/", views.view_profile, name="view"),
	path("<int:pk>/edit/", views.edit_page, name="edit"),
	path("delete/<int:pk>/", views.delete_profile, name="delete"),
	path("ask/<int:pk>/", views.ask_confirm, name="ask"),
	path("create/<int:pk>/", views.create_profile, name="createprofile"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)