from django.shortcuts import render

nav = [
    ['/blog/vylona', 'Vylona'],
    ['/blog/budy', 'Budi'],
    ['/blog/jordan', 'Jordan'],
    ['/blog/flower', 'Flower'],
]
# Create your views here.
def index(request) :
    context = {
        'title' : 'blog',
        'author' : 'random',
        'nav' : nav,
    }
    return render(request, 'index.html', context)

def vylona(request) :
    context = {
        'title' : 'Vylona',
        'author' : 'vylona',
        'nav' : nav,
    }
    return render(request, 'blog/index.html', context)

def budy(request) :
    context = {
        'title' : 'Budy',
        'author' : 'budy',
        'nav' : nav,
    }
    return render(request, 'blog/index.html', context)

def jordan(request) :
    context = {
        'title' : 'Jordan',
        'author' : 'jordan',
        'nav' : nav,
    }
    return render(request, 'blog/index.html', context)

def flower(request) :
    context = {
        'title' : 'Flower',
        'author' : 'flower',
        'nav' : nav,
    }
    return render(request, 'blog/index.html', context)