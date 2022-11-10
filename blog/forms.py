from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ["title", "body", "image", "status", 'tag']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields['body']:
                continue

        if self.fields['tag'] and self.fields['status'] and self.fields['image']:
            self.fields['tag'].widget.attrs['class'] = 'form-select'
            self.fields['status'].widget.attrs['class'] = 'form-select'
            self.fields['image'].widget.attrs['class'] = 'input-group-text'

        self.fields['image'].widget.attrs['accept'] = "image/png, image/gif, image/jpeg"
    # self.fields['upload_book'].widget.attrs['accept'] = '.pdf'
