from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def shirt(request):
    return render(request,'shirt/shirt.html')

def profile(request):
    return render(request,'profile/profile.html')
