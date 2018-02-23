from django.shortcuts import render

def index_view(req):
    return render(req, 'page.html', {
        'data': "My first django page!",
        'title': "Eason web",
        })
