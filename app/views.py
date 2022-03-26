from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import MyUserCreationForm
from app.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')
  
#=-------register function-------

def register(request):

##======= Using UserCreation Form method=======
    '''
	form = MyUserCreationForm()
	if request.method =='POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			user  = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			login(request, user)
			return redirect('/')
		else:
			messages.error(request, 'An error occured during registration')

	return render(request, 'signup.html', {'form' : form})

	'''
#=======Custom method========

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_pass = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exist!!')
            return redirect('register')
            # return HttpResponse("Username Already Exist")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email Id Already Exist!!")
            return redirect("register")
            # return HttpResponse("Email Id Already Exist")

        elif password == con_pass:

            user =User(username=username,email=email,password=password)
            user.save()
            login(request, user)
            # return HttpResponse("saved")
            return redirect('/')
        else:
            return HttpResponse("Password Not Matching")
    else:
        return render(request,'signup.html')
	
#============loginform=============

def loginForm(request):
    
    page = login
    # if request.user.is_authenticated:
    #     return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username, password=password)
            login(request, user)
            return redirect("/")
        except User.DoesNotExist:
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,'Invalid Username or Password')
                return redirect('login')
    else:
        context = {'page':page}
        return render(request, 'login.html',context)


#===log out===

def logoutForm(request):
    logout(request)
    return redirect('/')