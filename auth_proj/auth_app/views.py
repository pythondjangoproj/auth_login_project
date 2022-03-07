from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import signupform
from . import forms
from django.http import HttpResponseRedirect

# Create your views here.

def home_view(request):
    return render(request, 'auth_app/home.html')

@login_required
def javaexam_view(request):
    return render(request, 'auth_app/javaexam.html')

@login_required
def pythonexam_view(request):
    return render(request, 'auth_app/pythonexam.html')


def signup_view(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        User=form.save()
        User.set_password(user.password)
        User.save()
        return HttpResponseRedirect('accounts/login')
    return render(request,'auth_app/signup.html',{'form':form})

def logout_view(request):
    return render(request,'auth_app/logout.html')