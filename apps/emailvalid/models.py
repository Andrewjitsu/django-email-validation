from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, post):
    	errors=[]
    	if len(post['email'])==0:
    		errors.append("Email field must not be empty.")
    	elif not EMAIL_REGEX.match(post['email']):
    		errors.append("Email is invalid. Please try again.")
    	return errors

class User(models.Model):
	email=models.CharField(max_length=200)
	updated_at=models.DateTimeField(auto_now_add=True)
	created_at=models.DateTimeField(auto_now=True)
	objects=UserManager()


          
      