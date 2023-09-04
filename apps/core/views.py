from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.job.models import Job
from apps.userprofile.models import Userprofile
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import *


def base(request):
    return render(request,'base.html')

def frontpage(request):
    jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')[0:3]
    return render(request, 'core/frontpage.html', {'jobs': jobs})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')

            if account_type =='employer':
                userprofile = Userprofile.objects.create(user=user, is_employer=True) 
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user) 
                userprofile.save()
        return render(request,'login.html')    

            
        
    else:    
        form = UserCreationForm()
    
# def login(request):
#     error=""
#     if request.method =="POST":
#         u = request.POST['uname'];
#         p = request.POST['pwd'];
#         user = authenticate(username=u , password= p)
#         if user:
            
#                 user1= user.objects.get(user=user)
#                 login(request,user)
#         else:
#             error="yes"
#     d={'error': error}        
     
    
    
    return render(request, 'core/signup.html', {'form' : form})