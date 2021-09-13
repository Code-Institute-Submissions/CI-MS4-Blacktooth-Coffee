from django import forms
from .models import Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body']
