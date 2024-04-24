
from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car


# Create your views here.

class CarList(ListView):
    model = Car

class CarDetail(DetailView):
    model = Car
    
class CarCreate(CreateView):
    model = Car
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('car_list')

class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('car_list')

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')

   
   
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request, 'Cars/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('car_list')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'Cars/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')