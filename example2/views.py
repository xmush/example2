from django.shortcuts import render


def index(request) :
    context = {
        'title' : 'Beranda',
        'author' : 'xmush',
    }
    return render(request, 'index.html', context)

def about(request) :
    context = {
        'title' : 'About',
        'author' : 'xmush1',
    }
    return render(request, 'index.html', context)

def contact(request) :
    context = {
        'title' : 'Contact',
        'author' : 'xmush2',
    }
    return render(request, 'index.html', context)