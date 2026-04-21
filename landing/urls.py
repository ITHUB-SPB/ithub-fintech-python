from django.urls import path
from .views import home_view, about_view, contacts_view, create_view, delete_view, edit_view

urlpatterns = [
    path('', home_view, name="home"),
    path('create', create_view, name="create"),
    path('edit/<int:id>', edit_view, name="edit"),
    path('delete/<int:id>', delete_view, name="delete"),
    path('about', about_view, name="about"),
    path('contacts', contacts_view, name="contacts")
]
