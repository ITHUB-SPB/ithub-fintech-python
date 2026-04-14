from django.urls import path
from .views import home_view, about_view, contacts_view, create_view

urlpatterns = [
    path('', home_view, name="home"),
    path('create', create_view, name="create"),
    path('about', about_view, name="about"),
    path('contacts', contacts_view, name="contacts")
]
