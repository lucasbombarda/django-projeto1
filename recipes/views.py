from django.shortcuts import render
from utils.recipes.factory import makerecipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [makerecipe() for _ in range(10)]
    })


def recipes(request, id):
    return render(request, 'recipes/pages/recipes-view.html', context={
        'recipe': makerecipe(),
        'is_detail_page': True,
    })
