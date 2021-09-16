from django import forms
from .models import User
from django.utils.safestring import mark_safe


class PictureWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        img_html = mark_safe(f'<img height = "200px" width = "200px" src="{value.url}"/><br>')
        return f"{img_html}{input_html}"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "avatar",
            "first_name",
            "last_name",
            "about",
            "twitter_id",
            "facebook_id",
            "birth_date",
        )
    birth_date = forms.DateField()
    input_formats = ['%Y-%m-%dT%H:%M'],
    widget = forms.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'class': 'form-control'},
        format='%Y-%m-%dT%H:%M')
    avatar = forms.ImageField() #widget=PictureWidget
