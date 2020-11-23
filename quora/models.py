from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	pic = models.ImageField(null=True,blank=True,upload_to='profile_pics/')

	def __str__(self):
		return self.user.username

     

