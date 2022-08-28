from django.contrib import admin
from django.urls import include, path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
