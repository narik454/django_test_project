from django.shortcuts import render
from goods.models import Categories

def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Чёрное Белое - Главная',
        'content': 'Фотостудия Чёрное Белое',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Чёрное Белое - О нас',
        'content': 'Фотостудия Чёрное Белое, о нас',
        'text_on_page': 'TEXTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    }
    return render(request, 'main/about.html', context)