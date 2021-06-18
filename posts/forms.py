from django import forms
from .models import Comment, Post, Tag
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Text here...", "rows": 1, "cols": 25}),
    )

    class Meta:
        model = Comment
        fields = ("body",)


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ("preview_pic", "title", "body",  "is_published", "tag")


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)


class SearchForm(forms.Form):
    query = forms.CharField()
