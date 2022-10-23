from django import forms
from .models import BlogReview


class ReviewForm(forms.ModelForm):
	class Meta:
		model = BlogReview
		fields = ["starts", "comment"]


	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)


		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
