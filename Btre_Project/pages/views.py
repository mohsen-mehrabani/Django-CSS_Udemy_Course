from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return HttpResponse('<h1>This is my first page</h1>')

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')

