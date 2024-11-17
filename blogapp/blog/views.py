from django.http.response import HttpResponse
from django.shortcuts import render

data = {
    "blogs": [
        {
        "id": 1,
        "title": "Python Programlama",
        "img": "python-logo.png",
        "is_active": True,
        "is_home": False,
        "description": "Python programlama dili hakkında bilgiler",
        },
        {
        "id": 2,
        "title": "React Programlama",
        "img": "react-logo.png",
        "is_active": True,
        "is_home": True,
        "description": "React programlama dili hakkında bilgiler",
        },
        {
        "id": 3,
        "title": "Angular Programlama",
        "img": "angular-logo.png",
        "is_active": False,
        "is_home": True,
        "description": "Angular programlama dili hakkında bilgiler",
        }
    ]
}

# Create your views here.

def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, 'blog/index.html', context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, 'blog/blogs.html', context)

def blog_details(request, id):

    # blogs = data["blogs"]
    # selectedBlog = None

    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    #         break
    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0]

    return render(request, 'blog/blog-details.html', {
        'blog': selectedBlog
    })
