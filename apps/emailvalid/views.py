from django.shortcuts import render, redirect
from .models import User
import re
from django.contrib import messages

def index(request):
	return render(request, "emailvalid/index.html")

def add_user(request):
	email_errors=User.objects.validate(request.POST)
	if len(email_errors)>0:
		for error in email_errors:
			messages.error(request, error)
		return redirect('/')
	else:
		User.objects.create(email=request.POST['email'])
		return redirect('/success')

def success(request):
	context={
	"users":User.objects.all()
	}
	return render(request, "emailvalid/success.html", context)
