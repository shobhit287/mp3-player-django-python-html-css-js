from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('mp3/choice/<str:slug>',views.filter_choice,name="filterchoice"),
    path('mp3/search',views.search,name="search"),
    path('mp3/signup',views.handlesignup,name="signup"),
    path('mp3/login',views.handlelogin,name="login"),
    path('mp3/logout',views.handlelogout,name="logout"),
    path('mp3/addfav/<int:id>',views.addfav,name="addfav"),
    path('mp3/rem_fav/<int:id>',views.remfav,name="addfav"),
]
