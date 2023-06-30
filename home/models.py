from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#creating more attirbutes to user models present in Django admin

class user_model(models.Model):

    user=models.OneToOneField(User,on_delete=any)
    # first_name, last_name, email, password are the primary attributes present in User
    
    #adding new attirbutes

    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to="profile_pic", blank=True)

    def __str__(self) -> str:
        return self.user.username
