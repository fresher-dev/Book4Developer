from django import forms
from .models import BlogComment



class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ["email", "body"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'