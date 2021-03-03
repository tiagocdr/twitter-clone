from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from authentication.form import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from twitteruser.models import TwitterUser
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'form.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create(
                username=data['username'], password=data['password']
                )
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('home'))
                )
            
    form = SignUpForm()
    return render(request, 'form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))