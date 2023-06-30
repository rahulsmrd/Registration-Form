from django import forms
from django.contrib.auth.models import User
from home.models import user_model

class User_display(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username', 'email', 'password')

class userProfileInfo(forms.ModelForm):
    class Meta:
        model=user_model
        fields=('portfolio_site', 'profile_pic')