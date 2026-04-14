from django.shortcuts import render
from .models import RecordType

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')
