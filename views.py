
from django.http import HttpResponse
from django.shortcuts import render
import requests

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def hello(request):
    context = {
        'text': 'Hello cooker',
    }
    return render(request, 'hello.html',context)


def cook_dishes(request, dish):
    recipe = {}
    servings = int(request.GET.get("servings",1))
    if servings > 1:
        for ingred, amount in DATA[dish].items():
            recipe[ingred] = amount*servings
    else:
        recipe = DATA[dish]

    context = {
        'recipe':  recipe
    }
    return render(request, 'dishes.html', context)



#
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


