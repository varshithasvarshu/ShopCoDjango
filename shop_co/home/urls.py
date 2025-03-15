from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shirt/',views.shirt,name='shirt'),
     path('profile/', views.profile, name='profile')
]