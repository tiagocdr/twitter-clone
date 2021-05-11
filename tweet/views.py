from django.shortcuts import render, redirect
from tweet.form import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notifications
from django.contrib.auth.decorators import login_required
import re
# Create your views here.

def mention_helper(content, tweet):
    ''' 
    Will take care of creating the notifications if 
    a mention is present in the content.
    '''
    pattern = r'(@\w+)'
    m = re.findall(pattern, content)
    users = TwitterUser.objects.all()
    users = [user.username for user in users]
    if m:
        for p in m:
            if p[1:] in users:
                user = TwitterUser.objects.get(username=p[1:])
                noti = Notifications.objects.create(
                    tweet= tweet,
                    mentioned_user=user,
                )
                print(noti)

            

@login_required
def post_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            tweet = Tweet.objects.create(user=request.user,
                content=data['content']
                )
            mention_helper(data['content'], tweet)
            return redirect('/')
    form = TweetForm()
    return render(request, 'addtweet.html', {'form': form})

def tweet_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet.html', {'tweet': tweet})
