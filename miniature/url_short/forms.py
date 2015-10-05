from django import forms
from .models import Link

class URLShortenForm(forms.Form):
    url = forms.URLField(label='URL', required=True)


