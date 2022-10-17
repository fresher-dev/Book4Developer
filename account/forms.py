from django import forms
from .models import Profile




class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['username', 'email', 'description', 'phone', 'address', 'image']
		#fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)


		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


		self.fields['image'].widget.attrs['accept'] = "image/png, image/gif, image/jpeg"