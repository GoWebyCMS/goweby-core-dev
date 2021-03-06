from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from itertools import chain
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.db.models import Count

from .forms import SearchForm
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

def post_list(request, tag_slug=None):
    # grub post list as an object list for pagenation
    object_list = Post.published.all()

    # Tags: let user list all posts tagged with a specific tag
    tag = None
    if tag_slug:
         tag = get_object_or_404(Tag, slug=tag_slug)
         object_list = object_list.filter(tags__in=[tag])

    # Pagenation

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



    # TODO: fetch limited latest projects for the related sidebar widjet

    return render(request, 'blog/post/list.html', {
            'posts': posts,
            'page' : page,
            'tag' : tag,
            })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.all()

    # retrieve a list of similar posts filtering by tag
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    return render(request, 'blog/post/detail.html',
                                {
                                    'post': post,
                                    'similar_posts': similar_posts,
                                })

def post_search(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Post).filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
    return render(request,
            'blog/post/search.html',
            {'form': form,
            #'cd': cd,
            #'results': results,
            #'total_results': total_results
            })
