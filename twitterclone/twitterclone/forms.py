from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.Form):
    username= forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password= forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    bio= forms.CharField(max_length= 300)

