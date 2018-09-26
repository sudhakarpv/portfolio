from django.shortcuts import render, get_object_or_404
from .models import blog


def allblogs(request):
    blogs = blog.objects
    return(render(request, 'blog/blog.html', {'blogs': blogs}))


def details(request, blog_id):
    detailblog = get_object_or_404(blog, pk=blog_id)
    return (render(request, 'blog/details.html', {'blog': detailblog}))
