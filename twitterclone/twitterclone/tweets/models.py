from django.db import models
from twitterclone.twitterusers.models import Profile

class Tweet(models.Model):
    tweet= models.TextField(max_length= 140)
    timestamp = models.DateTimeField(auto_now_add= True)
    user= models.ForeignKey(Profile, blank=True, null=True, on_delete = models.CASCADE, related_name='tweets')

    def __str__(self):
        return self.tweet