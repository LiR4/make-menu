from django.shortcuts import render
from app_menu import functions

def Home(request):
    return render(request, 'clientes/Home.html')

def Menu(request):
    search = functions.menuInfo
    url = request.POST.get('tabelaUrl')
    title = request.POST.get('nomeL')
    global First
    First = {
        'url': url,
    }
    search.getData(First)
    global infos
    infos = {
        'title': title,
        'Salgados': search.getCategory('Salgado'),
        'Doce': search.getCategory('Doce'),
        'Bebidas' : search.getCategory('Bebidas')
    }
    

    return render(request, 'clientes/Menu.html', infos)


