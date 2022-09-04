from django.shortcuts import render
from utils.recipes.factory import makerecipe

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def recipes(request, id):
    return render(request, 'recipes/pages/recipes-view.html', context={
        'recipe': makerecipe(),
        'is_detail_page': True,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })
