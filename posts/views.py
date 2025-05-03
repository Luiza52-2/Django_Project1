from django.shortcuts import render, HttpResponse
from random import randint

def index(request):
    return HttpResponse(f"Hello, world. {randint(1,100)}")

def html_view(request):
    return render(request, "test.html")

# Create your views here.
