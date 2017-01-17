from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import  Project, ProjectCategory, Skill

# Create your views here.


# TODO: Find out how to UT test a class based view
# class PortfolioListView(ListView):


def portfolio_list(request):
    object_list = Project.objects.filter(end_date__lte=timezone.now()).order_by('-end_date')
    categories = Project.objects.all()

    # pagenation
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        projects = paginator.page(paginator.num_pages)

    return render(request, 'portfolio/list.html',
                {
                    'projects': projects,
                    'categories': categories,
                    'page': page,
                })

def portfolio_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(
        request,
        'portfolio/portfolio_detail.html',
        {
            'project': project,
        }
    )
