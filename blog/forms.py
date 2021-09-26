from django import forms
from django.core import validators
from .models import *


class PRForm(forms.Form):
    company_name = forms.CharField(label='COMPANY NAME', max_length=100, required=True)
    email = forms.EmailField(label='EMAIL ADDRESS', max_length=100, validators=[validators.EmailValidator],
                             required=True)
    image = forms.ImageField(label='PRESS RELEASE IMAGE', widget=forms.ImageField, required=True)
    heading = forms.CharField(label='PRESS RELEASE HEADING', max_length=500)
    description = forms.CharField(label='PRESS RELEASE DESCRIPTION', widget=forms.Textarea)

    class Meta:
        model = PressRelease
        # fields = ('company_name', 'email', 'image', 'heading', 'description')


class W4UForm(forms.Form):
    company_name = forms.CharField(label='COMPANY NAME', max_length=100, required=True)
    email = forms.EmailField(label='EMAIL ADDRESS', widget=forms.TextInput(attrs={'id': 'email'}), max_length=100,
                             validators=[validators.EmailValidator],
                             required=True)
    image = forms.ImageField(label='PRESS RELEASE IMAGE', required=True)  # widget=forms.ImageField,
    heading = forms.CharField(label='PRESS RELEASE HEADING', max_length=500)
    description = forms.CharField(label='PRESS RELEASE DESCRIPTION', widget=forms.Textarea)

    class Meta:
        model = WriteForUs
        # fields = ('company_name', 'email', 'image', 'heading', 'description')
