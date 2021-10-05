from django.shortcuts import render

# Create your views here.
def index(request) :
    context = {
        'title' : 'blog',
        'author' : 'random',
    }
    return render(request, 'blog/index.html', context)

def loadmore(request) :
    context = {
        'title' : 'loadmore',
        'author' : 'vylona',
    }
    return render(request, 'blog/index.html', context)