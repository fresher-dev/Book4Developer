from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['description', 'phone', 'address', 'image', "website", "github", "twitter", "instagram", "facebook"]
		#fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)


		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


		self.fields['image'].widget.attrs['accept'] = "image/png, image/gif, image/jpeg"


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)


	class Meta:
		model = User 
		fields = ["username", "email", "password1", "password2"]

	
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)


		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


