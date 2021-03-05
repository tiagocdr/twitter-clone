from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser
# Create your models here.

# TODO: Filter homepage by followings and datetime.
class Notifications(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)
    mentioned_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return 'Mention: ' + str(self.mentioned_user.username) + ' is read?: ' + str(self.is_read)
    ...