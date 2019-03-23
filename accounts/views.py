from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
	name='Harsha Deuri'
	numbers=[1,2,3,4,5]
	args={'myName':name, 'myNumbers':numbers}
	return render(request,'accounts/landingPage.html',args)

def register(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:login'))
	else:
		form=RegistrationForm()

	args={'form':form}
	return render(request, 'accounts/registration.html', args)

def profile(request):
	args={'user':request.user}

	return render(request, 'accounts/profile.html', args)