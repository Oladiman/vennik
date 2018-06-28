from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request ,'vennik/index.html')
    
def home(request):
    return render(request, 'vennik/home.html')

def products(request):
    return render(request, 'vennik/products.html')

def login(request):
    return render(request,'vennik/login.html')

def logout(request):
    return render(request,'vennik/logout.html')

def register(request):
    return render(request,'vennik/register.html')    

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

