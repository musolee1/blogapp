from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog


data = {
    "blogs": [
        {
        "id": 1,
        "title": "Python Programlama",
        "image": "python-logo.png",
        "is_active": True,
        "is_home": False,
        "description": "Python programlama dili hakkında bilgiler",
        },
        {
        "id": 2,
        "title": "React Programlama",
        "image": "react-logo.png",
        "is_active": True,
        "is_home": True,
        "description": "React programlama dili hakkında bilgiler",
        },
        {
        "id": 3,
        "title": "Angular Programlama",
        "image": "angular-logo.png",
        "is_active": False,
        "is_home": True,
        "description": "Angular programlama dili hakkında bilgiler",
        }
    ]
}

# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
    }
    return render(request, 'blog/index.html', context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, 'blog/blogs.html', context)

def blog_details(request, id):
    
    blog = Blog.objects.get(id = id)

    return render(request, 'blog/blog-details.html', {
        'blog': blog
    })
