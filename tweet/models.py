from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    timestamp = models.DateTimeField(default=timezone.now)