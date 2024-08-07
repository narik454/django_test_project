from django.shortcuts import render

def index(request):
    

    context = {
        'title': 'Чёрное Белое - Главная',
        'content': 'Фотостудия Чёрное Белое',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Чёрное Белое - О нас',
        'content': 'Фотостудия Чёрное Белое, о нас',
        'text_on_page': 'TEXTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    }
    return render(request, 'main/about.html', context)