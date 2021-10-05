from django.shortcuts import render

nav = [
    ['/', 'Beranda'],
    ['/about' , 'About'],
    [ '/blog', 'Blog'],
    ['/contact', 'Contact'],
]

def index(request) :
    context = {
        'title' : 'Beranda',
        'author' : 'xmush',
        'nav' : nav,
    }
    return render(request, 'index.html', context)

def about(request) :
    context = {
        'title' : 'About',
        'author' : 'xmush1',
        'nav' : nav,
    }
    return render(request, 'index.html', context)

def contact(request) :
    context = {
        'title' : 'Contact',
        'author' : 'xmush2',
        'nav' : nav,
    }
    return render(request, 'index.html', context)