from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.
def userReg(request):
    return render(request, "users/registration.html")

def userLogout(request):
	logout(request)
	messages.success(request, "You've successfully logged Out. Thanks for visiting our website today")
	return redirect("commerce:index")


def userLogin(request):
	if request.method == 'POST':
		username = request.POST.get('email')
		password = request.POST.get('password')
		Username = ''
		user = User.objects.filter(email__exact = username)

		if user.exists():
			currentUser = User.objects.get(email = username)
			Username = currentUser.username
		else:
			messages.warning(request, 'Email does not exist')
			return redirect('users:userReg')
		
		user = authenticate(username = Username, password = password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been successfully logged in")
			return redirect('chat:chatIndex')
		else:
			messages.warning(request, "Couldn't login user")
			return redirect('users:userReg')
	else:
		return redirect('users:userReg')

def userSignup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        #username = request.POST.get('email')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        recovery = request.POST.get('recovery')
        location = request.POST.get('location')
        
        user = User.objects.create_user(username = email, password = password, email = email)
        user.save()
        
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        
        user.profile.phone = phone
        user.profile.recovery = recovery
        user.profile.location = location
        user.save()
        
        messages.success (request, "User successfully Created")
        return redirect ("users:userLogin")
    else:
        return render(request, 'users/signup.html')


