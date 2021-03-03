from django.shortcuts import render
from twitteruser.models import TwitterUser

# Create your views here.

def landing_view(request):
    return render(request, 'landing.html')