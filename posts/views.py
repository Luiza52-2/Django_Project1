from django.shortcuts import render, HttpResponse, redirect
from random import randint
from posts.models import Post
from posts.forms import PostForm

def index(request):
    return HttpResponse(f"Hello, world. {randint(1,100)}")

def homepage_view(request):
    return render(request, "base.html")

def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={'posts': posts})

def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.filter(id=post_id).first()
        return render(request, 'posts/post_detail.html', context={'post': post})

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Теперь используется ModelForm
            return redirect('/posts/')
    else:
        form = PostForm()

    return render(request, "posts/post_create.html", context={'form': form})
