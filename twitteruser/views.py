from django.shortcuts import redirect, render
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notifications
from django.contrib.auth.decorators import login_required
# Create your views here.
# request.user.id
# get following users id 
# request.user.following
# tweet can be an array, add to it by looping trough the following ids and getting the tweet, then sendind that
# on the context
@login_required
def landing_view(request):
    tweets = Tweet.objects.all().order_by('-timestamp')
    tweets = [tweet for tweet in tweets if tweet.user in request.user.following.all() or request.user == tweet.user]
    context = {'tweets': tweets}
    if request.user.is_authenticated:
        user = TwitterUser.objects.get(id=request.user.id)
        followers = len(user.followers.all())
        mentions = Notifications.objects.filter(
            mentioned_user=request.user,
            is_read=False
            )
        context.update({'followers': followers, 'notis': len(mentions)})
    return render(request, 'landing.html', context)

def user_view(request, user_id):
    user = TwitterUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user=user).order_by('-timestamp')
    is_follower = request.user in user.followers.all()
    context = {
        'tweets': tweets,
        'user': user,
        'is_follower': is_follower,
        'num_tweets': len(tweets)
        }
    return render(request, 'user.html', context)

@login_required
def follow_user(request, user_id):
    user = request.user
    to_follow = TwitterUser.objects.get(id=user_id)
    user.following.add(to_follow)
    user.save()
    to_follow.followers.add(user)
    to_follow.save()
    return redirect(f'/user/{user_id}')

@login_required
def unfollow_user(request, user_id):
    user = request.user
    to_unfollow = TwitterUser.objects.get(id=user_id)
    user.following.remove(to_unfollow)
    user.save()
    to_unfollow.followers.remove(user)
    to_unfollow.save()
    return redirect(f'/user/{user_id}')

