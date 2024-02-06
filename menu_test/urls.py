from django.contrib import admin
from django.urls import path, re_path
from .views import show_menu_test

urlpatterns = [
    path('', show_menu_test, name='show_menu_test'),
    re_path(r'^[/a-zA-Z0-9]+$', show_menu_test, name='show_menu_test'),
]