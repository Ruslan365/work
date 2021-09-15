from django import forms
from .models import Comment, Post, Tag
from django_summernote.widgets import SummernoteWidget
from django.utils.safestring import mark_safe



class PictureWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        img_html = mark_safe(f'<img height = "200px" width = "200px" src="{value.url}"/><br>')
        return f"{img_html}{input_html}"



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
    title = forms.TextInput()

    tag = forms.CharField(max_length=255)

    # description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ("preview_pic", "title", "description", "body",  "is_published", "tag")

    # preview_pic = forms.ImageField(widget=PictureWidget)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)


class SearchForm(forms.Form):
    query = forms.CharField()
