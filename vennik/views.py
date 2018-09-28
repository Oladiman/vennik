from django.shortcuts import render,redirect
from vennik.forms import RegistrationForm
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def index(request):
    return render(request ,'vennik/index.html')
    
def home(request):
    return render(request, 'vennik/home.html')

def products(request):
    return render(request, 'vennik/products.html')

def login(request):
    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid:
            return render(request,'vennik/login.html')

def logout(request):
    return render(request,'vennik/logout.html')


def view_profile(request):
    args={'user':request.user}
    return render(request,'vennik/profile.html',args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST,instance=request.user )
        if form.is_valid():
            form.save()
            return redirect('/vennik/profile.html') 
        else:
            form=UserChangeForm(instance=request.user)
            args={'form':form}
            return render(request,'vennik/edit_profile.html',args)       


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vennik')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'vennik/register.html',args)    

def contact(request):
    return render(request, 'vennik/contact.html')

def single(request):
    return render(request,'vennik/single.html')   

def self_contain(request):
    return render(request,'vennik/self-contain.html')

def single_room(request):
    return render(request,'vennik/single-room.html') 

def exclusive(request):
    return render(request, 'vennik/exclusive-suites.html')


def goods(request):
    return render(request, 'vennik/goods.html')


def campus(request):
    return render(request, 'vennik/campus.html')


def human(request):
    return render(request, 'vennik/human-services.html')

def undeveloped(request):
    return render(request, 'vennik/undeveloped-land.html')

def properties(request):
    return render(request, 'vennik/properties-for-sale.html')

