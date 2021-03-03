from django.shortcuts import render
from twitteruser.models import TwitterUser
from tweet.models import Tweet
# Create your views here.
# request.user.id
# get following users id 
# request.user.following
# tweet can be an array, add to it by looping trough the following ids and getting the tweet, then sendind that
# on the context
def landing_view(request):
    tweets = Tweet.objects.get()
    return render(request, 'landing.html')