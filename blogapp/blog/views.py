from django.http.response import HttpResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Category
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all(),
        "latest": Blog.objects.filter(is_home=True, is_active=True).order_by('-blog_date')
    }
    return render(request, 'blog/index.html', context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, 'blog/blogs.html', context)

def blog_details(request, slug):
    
    blog = Blog.objects.get(slug = slug)

    return render(request, 'blog/blog-details.html', {
        'blog': blog
    })

def blogs_by_category(request, slug):
        context = {
            "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
            # "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
            "categories": Category.objects.all(),
            "selected_category": slug
        }
        return render(request, 'blog/blogs.html', context)



def BlogPostLike(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('blog_id'))
    post.likes.add(request.user)
    slug = post.slug
    return HttpResponseRedirect(reverse('blog_details', args=[slug]))

class BlogPostDetailView(DetailView):
    model = Blog
    template_name = 'blog-details.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Blog, id=self.kwargs['pk'])
        liked = False

        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data