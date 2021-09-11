from django import forms
from django.core import validators
from django_quill.fields import QuillField

from blog import models
from blog.models import Post


class PRForm(forms.Form):
    company_name = forms.CharField(max_length=100, required=True)
    industry = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, validators=[validators.EmailValidator], required=True)
    logo = forms.ImageField(widget=forms.ImageField, required=True)
    image = forms.ImageField(widget=forms.ImageField, required=True)
    address = forms.CharField(max_length=250, required=True)
    phone = forms.CharField(max_length=25)
    description = forms.CharField(widget=forms.Textarea)
    discount_description = forms.CharField(widget=forms.Textarea)
    release_date = forms.DateField(widget=forms.DateTimeField)
    sample = forms.FileField(widget=forms.FileField)
    facebook = forms.URLField(widget=forms.URLField)
    instagram = forms.URLField(widget=forms.URLField)
    twitter = forms.URLField(widget=forms.URLField)
    linkedin = forms.URLField(widget=forms.URLField)

    class Meta:
        model = models.PressReleaseForm
        fields = (
            'description',
        )

