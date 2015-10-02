from django import forms
from .models import Link

class URLShortenForm(forms.ModelForm):
    class Meta:
        model  = Link
        fields = ['url']


