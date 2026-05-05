from django import forms
from django.forms.widgets import Textarea

class ContactForm(forms.Form):
    theme = forms.CharField(min_length=3, max_length=15, required=True)
    message = forms.CharField(widget=Textarea, min_length=10, max_length=400, required=True)
    attachment = forms.FileField(required=False)