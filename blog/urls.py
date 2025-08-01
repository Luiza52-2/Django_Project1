"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import  post_list_view, homepage_view, post_detail_view, post_create_view, post_update_view, PostListClassView, PostDetailClassView
from django.conf.urls.static import static
from django.conf import settings
from users.views import register_view, login_view, logout_view, profile_view


urlpatterns = [
    path("", homepage_view),
    path('admin/', admin.site.urls),
    path('posts/', post_list_view),
    path('posts/class/', PostListClassView.as_view(), name='post_list_class_view'),
    path('posts/<int:post_id>/', post_detail_view),
    path('posts/class/<int:post_id>', PostDetailClassView.as_view(), name='post_detail_class_view'),
    path('posts/<int:post_id>/edit', post_update_view),
    path('posts/create/', post_create_view),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('profile/', profile_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
