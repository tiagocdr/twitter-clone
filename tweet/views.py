from django.shortcuts import render, redirect
from tweet.form import TweetForm
from tweet.models import Tweet
# Create your views here.

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