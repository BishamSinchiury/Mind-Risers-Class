from django.shortcuts import render # type: ignore
from django.http import HttpRequest # type: ignore

def index(request):
    return render(request, 'index.html')
