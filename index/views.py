from django.shortcuts import render

def index(req):
    return render(req, 'index/index.html', {
        'data': "My first django page!",
        'title': "Eason web",
        })
