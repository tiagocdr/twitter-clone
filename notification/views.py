from django.shortcuts import render

# Create your views here.

# Check for the text submited and find the @xxxx pattern
# if there is a user with that username notify them a
# Have the tweet show up in they notification section.

# notification view, takes the user and checks for tweets that have mentioned him 
# Notifications.objects.filter(mentioned_user=user), returns the tweets.

