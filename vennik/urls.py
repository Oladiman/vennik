from django.contrib import admin
from django.urls import path,re_path
from vennik import views
from django.contrib.auth.views import login,logout
urlpatterns = [
    path('index.html', views.index , name="index"),
    path('home.html', views.home, name='home'),
    path('', views.index ,name='index'),
    path('products.html', views.products, name='products'),
    # path('login.html' ,views.login ,name='login'),
    path('register.html',views.register ,name='register'),
    path('profile.html',views.view_profile,name='view_profile'),
    re_path(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    path('contact.html', views.contact ,name='contact'),
    path('single.html',views.single ,name='single'),
    path('self-contain.html',views.self_contain, name='self_contain'),
    path('single-room.html',views.single_room, name='single_room'),
    path('exclusive-suites.html', views.exclusive , name= 'exclusive'),
    path('campus.html',views.campus, name='campus'),
    path('goods.html',views.goods, name='goods'),
    path('human-services.html',views.human,name='human'),
    path('undeveloped-land.html',views.undeveloped,name='undeveloped'),
    path('properties-for-sale.html',views.properties,name='properties'),
    path('login.html',login,{'template_name':'vennik/login.html'}),
    path('logout.html',logout,{'template_name':'vennik/logout.html'})
]