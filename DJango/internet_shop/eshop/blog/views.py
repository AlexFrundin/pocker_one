from django.shortcuts import render, get_object_or_404
from .models import Post

def details(request,date,slug):
    post=get_object_or_404(Post, slug=slug, date=date)
    return render (request, 'post_detail.html',
    {
        'post':post
    })

def posts (request):
    post= Post
