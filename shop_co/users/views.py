from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import User, Profile
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request,'home/home.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists():
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=make_password(password)
            )
            user.save()
        return redirect('login')
        
        
        # Save Profile
        profile = Profile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        
        messages.success(request, "Account created successfully!")
        return redirect('login')
    
    return render(request, 'users/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password.')
            return render(request,'users/login.html')


    return render(request, 'users/login.html')