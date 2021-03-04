from django.shortcuts import render, redirect
from tweet.form import TweetForm
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def post_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(user=request.user,
                content=data['content']
                )
            return redirect('/')
    form = TweetForm()
    return render(request, 'addtweet.html', {'form': form})

def tweet_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet.html', {'tweet': tweet})
