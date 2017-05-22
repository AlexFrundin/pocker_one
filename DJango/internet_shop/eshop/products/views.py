from django.shortcuts import render, get_object_or_404,redirect
from django.http.response import HttpResponse
import random
from django.contrib import messages
from .models import Product, Feedback
from .forms import FeedbackForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
# def index(request):
#     return HttpResponse("I LOve Python!!!")
def index(request):
    return render(request, 'index.html', {'rand':random.randint(1,10)})


@login_required(login_url='/')
def show_all(request):
    p=Paginator(Product.objects.order_by("pk").all(),2)
    page=int(request.GET.get('page',1))
    return render(
    request,
    "show_all.html",
    {
    'products':p.page(page)
    }
    )

@login_required(login_url='/')
def detail(request, product_id):
    form=FeedbackForm()
    product = get_object_or_404(Product, pk = int(product_id))
    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(
            nick=form.cleaned_data["nick"],
            feedback=form.cleaned_data['feedback'],
            product = product,)
            messages.success(request,'Feedback is add')
            return redirect('/products/detail/'+product_id)
    return render(
    request, 'detail.html',
    {'product': product,
    'form':form,
    'feedbacks':Feedback.objects.filter(product=product)}
    )
