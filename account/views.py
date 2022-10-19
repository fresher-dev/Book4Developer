from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NewUserForm
from django.urls import reverse
# Create your views here.


def home(request):
	return render(request, 'account/home.html', {'all': User.objects.all()})

def singin(request):
	if request.method == "POST":
		name = request.POST['username']
		password1 = request.POST['password1']
		print(name, password1)
		user = authenticate(request, username=name, password=password1)
		if user is None:
			return HttpResponse("Invalid credentials.<br>User not found!")
		if user is not None:
			login(request, user)
			messages.success(request, "login successfully!")
			return redirect("home") # go to home 
		else:
			messages.info(request, "Wrong username and password")
			return redirect("login")

	return render(request, 'account/login.html')



def singup(request):
	if request.method == "POST":
		
		form = NewUserForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Account successfully created!")
			return redirect("home")
	else:
		form = NewUserForm()
		messages.info(request, "Wrong password!")

	context = {
		"form": form
	}	
	
	return render(request, "account/register.html", context)


def singout(request):
	logout(request)
	return redirect("login")


def view_profile(request, usr):
	user = User.objects.get(username=usr)

	profile = None
	
	for i in UserProfile.objects.all():
		if str(i) == str(user):
			profile = True
			break
		else:
			profile = None 

	a = str(request.user.username)
	b = str(user)


	check = None

	if str(request.user.username) == str(user):
		check = True
	else:
		check = False

	context = {
		"user": user,
		"check": check,
		"profile": profile,
	}

	return render(request, 'account/profile.html', context)


@login_required
def edit_page(request, pk):
	user = User.objects.get(id=pk)

	# UserProfile 
	usera = UserProfile.objects.get(user = user)

	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES, instance=usera)
		if form.is_valid():
			form.save()
			messages.success(request, "Update successfully!")
			return redirect(reverse("view", args=[user.username]))
	else:
		form = ProfileForm(instance=usera)

	context = {
		"form": form
	}

	return render(request, 'account/edit.html', context)



def delete_profile(request, pk):

	user = User.objects.get(id=pk)
	user.delete()
	return redirect("home")


def ask_confirm(request, pk):
	user = User.objects.get(id=pk)
	context = {
		"user": user,
	}
	return render(request, "account/ask.html", context)

@login_required
def create_profile(request, pk):

	user = User.objects.get(id=pk)
	print(user)
	if request.method == "POST":
		form = ProfileForm(request.POST)
		if form.is_valid():
			newform = form.save(commit=False)
			newform.user = user
			newform.save()
			messages.success(request, "Create profile successfully!")
			return redirect(reverse("view", args=[user.username]))
	else:
		form = ProfileForm()

	context = {
		"form": form
	}
	return render(request, "account/edit.html", context)