from django.shortcuts import render, HttpResponse
from random import randint
from posts.models import Post

def index(request):
    return HttpResponse(f"Hello, world. {randint(1,100)}")

def homepage_view(request):
    return render(request, "base.html")


# Create your views here.


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts.html", context={'posts':posts})