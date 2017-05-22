from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def log_in(request):
    if request.user.is_authenticated:
        return redirect( reverse('show_all'))
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(
        request,
        username=request.POST['name'],
        password=request.POST['passwd']
        )
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', reverse('show_all'))
            return redirect(next_url)
    return render (request, 'login.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect (reverse('login'))
