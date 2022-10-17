from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.urls import reverse
# Create your views here.


def home(request):
	return render(request, 'account/home.html', {'all': Profile.objects.all()})

def singin(request):
	if request.method == "POST":
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			user = authenticate(username=username, password=password1)
			if user is not None:
				login(request, user)
				messages.success(request, "login successfully!")
				return redirect("home") # go to home 
			else:
				messages.info(request, "Wrong username! Not Your Name")
				return redirect("login")
		else:
			messages.info(request, "Wrong username or password!")
			return redirect("login")

	return render(request, 'account/login.html')



def singup(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		slug = slugify(username)
		if password1 == password2:
			if Profile.objects.filter(username=username).exists():
				messages.info(request, "Username is already exits!")
				return redirect("register")
			if Profile.objects.filter(email=email).exists():
				messages.info(request, "Username is already exits!")
				return redirect("register")
			else:
				user = Profile.objects.create(username=username, email=email, password=password1, slug=slug)
				user.save()
				messages.success(request, "Account successfully created!")
				return redirect("login")

		else:
			messages.info(request, "Wrong password!")
			return redirect("register")


	return render(request, "account/register.html")


def singout(request):
	logout(request)
	return redirect("login")


def profile_page(request,pk):
	user = Profile.objects.get(id=pk)
	user_slug = user.slug


	context = {
		"user": user
	}

	return render(request, 'account/profile.html', context)


# enctype="multipart/form-data"

@login_required
def edit_page(request, pk):
	user = Profile.objects.get(id=pk)

	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, "Update successfully!")
			return redirect(reverse("profile", args=[user.id]))
	else:
		form = ProfileForm(instance=user)

	context = {
		"form": form
	}

	return render(request, 'account/edit.html', context)





