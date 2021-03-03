from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class TwitterUser(AbstractUser):
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_followers',
        blank=True
        )
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_following',
        blank=True
        )
    pass