from django.urls import path

from example.views import home


example_urls = [
    path('', home)]
