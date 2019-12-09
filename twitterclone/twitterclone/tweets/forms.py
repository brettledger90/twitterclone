from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    tweet = forms.CharField(required = True)

    class Meta:
        model = Tweet
        exclude = ['user','body',]