from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.


# TODO: Find out how to UT test a class based view
# class PortfolioListView(ListView):


def portfolio_list(request):
    return render(request, 'portfolio/list.html')

def portfolio_details(request, pk):
    return render(request, 'portfolio/details.html')
