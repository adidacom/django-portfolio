from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Blog
from pagedown.widgets import PagedownWidget


class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget(show_preview=False), label='Content')
    pub_date = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'd-inline-block col-md-3 col-sm-3'}),
        label='Publish Date')

    class Meta:
        model = Blog

        fields = [
            "title",
            "image",
            "video",
            "body",
            "draft",
            "pub_date",
        ]
        labels = {
            'pub_date': 'Publish Date',
            'title': 'Blog Title',
            'video': 'Video Link',
            'body': 'Content',
        }

        widgets = {
            "image": forms.ClearableFileInput(
                attrs={'class': "form-control mb-2 round"}
            ),
        }



