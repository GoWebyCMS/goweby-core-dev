from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

# TODO: Find out how to UT test a class based view
# class PortfolioListView(ListView):


def portfolio_list(request):
    return render(request, 'portfolio/portfolio_list.html')

def portfolio_details(request, pk):
    return render(request, 'portfolio/portfolio_details.html')
