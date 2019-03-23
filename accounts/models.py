from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.PROTECT)
	firstName=models.CharField(max_length=100,default='')
	lastName=models.CharField(max_length=100,default='')
	phone=models.IntegerField(default=0)
	courses=models.CharField(default='', max_length=100)

	

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)