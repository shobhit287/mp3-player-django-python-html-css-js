from django.shortcuts import render,HttpResponse,redirect
from .models import allsongs,Favourites
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib import messages
def index(request):
    if request.user.is_authenticated:
        slug="All Songs"
        fav_songs = Favourites.objects.filter(user=request.user).values_list('song', flat=True)
        all_songs=allsongs.objects.all()
        print(fav_songs)
        return render(request,'mp3_app/index.html',{'allsongs':all_songs,'favsongs':fav_songs,'slug':slug})
    else:
     all_songs=allsongs.objects.all()
     slug="All songs"
     return render(request,'mp3_app/index.html',{'allsongs':all_songs,'slug':slug})

def filter_choice(request,slug):
     if slug=="Favourites":
         if request.user.is_authenticated:
             fav_songs=Favourites.objects.filter(user=request.user)
             return render(request,'mp3_app/index.html',{'favsongs':fav_songs,'slug':slug})
         else:
             messages.error(request,"Log In Required")
             return redirect('/')
     else:        
      all_songs=allsongs.objects.filter(song_category=slug)
      return render(request,'mp3_app/index.html',{'allsongs':all_songs,'slug':slug})
 
def search(request):
   if request.user.is_authenticated: 
    if request.method=="GET":
        search_query = request.GET.get('search')
        all_songs = allsongs.objects.filter(Q(song_title__icontains=search_query) | Q(song_category__icontains=search_query))
        fav_songs = Favourites.objects.filter(user=request.user).values_list('song', flat=True)
    return render(request, 'mp3_app/index.html', {'allsongs': all_songs, 'slug': search_query,'favsongs':fav_songs,})
    
   else:
       search_query = request.GET.get('search')
       all_songs = allsongs.objects.filter(Q(song_title__icontains=search_query) | Q(song_category__icontains=search_query))
       return render(request, 'mp3_app/index.html', {'allsongs': all_songs, 'slug': search_query})
    
def handlesignup(request):
    if request.method=="POST":
      fname=request.POST.get('signupfname')
      lname=request.POST.get('signuplname')
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')
      myuser=User.objects.create_user(username,email,password)
      myuser.first_name=fname
      myuser.last_name=lname
      myuser.save()
      messages.success(request,"Your Account Created Successfully")
      return redirect('/')
    
    else:
        return HttpResponse("404 Verification Failed")
        
def handlelogin(request):
    if request.method=="POST":
        luname=request.POST.get('loginusername')
        lpass=request.POST.get('loginpassword')
        user=authenticate(request,username=luname,password=lpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In Success")
            return redirect('/')
        else:
             messages.error(request,"Wrong Credentials")   
             
    else: 
        return HttpResponse("404 Verification Failed ")         
    
def handlelogout(request):
    logout(request)
    messages.success(request,"Logged Out")
    return redirect('/')

def addfav(request,id):
    if request.user.is_authenticated:
       user=request.user
       song=allsongs.objects.filter(song_id=id)[0]
       add_fav=Favourites(user=user,song=song)
       add_fav.save()
       return redirect('/')
    else:
        messages.error(request,"Login Required for Add To Favorites")
        return redirect('/')
    
def remfav(request,id):
        user=request.user
        song=allsongs.objects.filter(song_id=id).first()
        Favourites.objects.filter(user=user,song=song).delete()
        messages.success(request,"Song Removed From Favourites")
        return redirect('/')
        
       
