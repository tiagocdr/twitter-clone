"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import login_view, logout_view, signup_view
from twitteruser.views import landing_view, user_view, follow_user, unfollow_user
from tweet.views import post_tweet_view

urlpatterns = [
    path('', landing_view, name='home'),
    path('user/<int:user_id>/', user_view,),
    path('follow/<int:user_id>/', follow_user,),
    path('unfollow/<int:user_id>/', unfollow_user,),
    path('tweetsomething/', post_tweet_view),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view), 
    path('admin/', admin.site.urls),
]
