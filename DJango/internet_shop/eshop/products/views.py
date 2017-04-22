from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
import random

from .models import Product

# Create your views here.
# def index(request):
#     return HttpResponse("I LOve Python!!!")
def index(request):
    return render(request, 'index.html', {'rand':random.randint(1,10)})

def show_all(request):
    return render(request, "show_all.html",
    {'products':Product.objects.all()})

def detail(request, product):
    return render( request, 'detail.html',
    {'product': get_object_or_404 (Product,pk =int(product))})
