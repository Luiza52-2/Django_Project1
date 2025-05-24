from django.shortcuts import render, HttpResponse, redirect
from random import randint
from posts.models import Post
from posts.forms import PostForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    return HttpResponse(f"Hello, world. {randint(1,100)}")

def homepage_view(request):
    return render(request, "base.html")

@login_required(login_url="/login/")
def post_list_view(request):
    form = SearchForm(request.GET)
    limit = 4
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = Post.objects.all()
        category_id = request.GET.get('category_id')
        ordering = request.GET.get('ordering')
        page = request.GET.get('page', 1)
        if category_id:
            posts = posts.filter(category_id=category_id)
        if search:
            posts = posts.filter (Q(title__icontains=search) | Q(content__icontains=search))
        if ordering:
            posts = posts.order_by(ordering)

        max_pages = len(posts) // limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) +1
        else:
            max_pages = round(max_pages)

        start = (int(page) - 1) * limit
        end = int(page) * limit
        posts = posts[start:end]
        context_data = {'posts': posts, 'form': form, 'max_pages':range(1, max_pages +1)}
        return render(request, "posts/post_list.html", context=context_data)

@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    
    if request.method == 'GET':
        post = Post.objects.filter(id=post_id).first()
        return render(request, 'posts/post_detail.html', context={'post': post})

@login_required(login_url="/login/")
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Теперь используется ModelForm
            return redirect('/posts/')
    else:
        form = PostForm()

    return render(request, "posts/post_create.html", context={'form': form})
