from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from itertools import chain
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

from .models import Post, Category, Tag

# Create your views here.
"""
class PostListView(ListView):
    queryset = []
    posts = Post.published.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    queryset = list(chain(posts, categories, tags))
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
"""

def post_list(request):
    # grub categories
    categories = Category.objects.all()
    # pagenation
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    # fetch limited latest projects for the related sidebar widjet
    return render(request, 'blog/post/list.html', {
            'posts': posts,
            'page' : page,
            'categories': categories,
            })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.all()


    return render(request, 'blog/post/detail.html',
                                {
                                    'post': post,
                                })
