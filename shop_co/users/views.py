from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Profile
from django.core.files.storage import default_storage

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # Create User
        user = User.objects.create(username=username, email=email, password=password)
        
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

        try:
            user = User.objects.get(username=username, password=password)
            if user:
                request.session['user_id'] = user.id  
                messages.success(request, "Login successful!")
                return redirect('home')
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, 'users/login.html')