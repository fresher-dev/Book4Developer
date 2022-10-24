from django import forms
from .models import BlogComment, BookComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ["email", "body"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class BookCommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = ["email", "body"]

    def __init__(self, *args, **kwargs):
        super(BookCommentForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
