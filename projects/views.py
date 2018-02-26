from django.shortcuts import render

def projects(req):
    return render(req, 'projects/projects.html', {
        'title': "Eason's Playground - Projects",
        })
