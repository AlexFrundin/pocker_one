from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.
# def index(request):
#     return HttpResponse("I LOve Python!!!")
def index(request):
    return render(request, 'index.html', {'rand':random.randint(1,10)})
