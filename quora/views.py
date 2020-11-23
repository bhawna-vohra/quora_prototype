from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm,UserFormLogin
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def post_list(request):
	return render(request,'quora/post_list.html',{})

def get_name(request):
	if request.method =='POST':
		form = NameForm(request.POST)

		if form.is_valid():
			return HTTPResponseRedirect('/thanks/')
	else:
		form = NameForm()
	return render(request,'quora/name.html',{'form':form})

def index(request):
	return render(request,'quora/index.html')

def register_view(request):
    registered = False

    if request.method == "POST":
    		user_form = UserForm(data=request.POST)
    		profile_form = UserProfileInfoForm(data=request.POST)

    		if user_form.is_valid() and profile_form.is_valid():

    		    user = user_form.save()
    		    user.set_password(user.password)
    		    user.save()

    		    profile = profile_form.save(commit=False)
    		    profile.user = user

    		    if 'pic' in request.FILES:
    		        profile.pic = request.FILES['pic']  

    		    profile.save()
    		    
    		    registered = True
    		else:
    		    print(user_form.errors,profile_form.errors)
    else:
    	    user_form = UserForm()
    	    profile_form = UserProfileInfoForm()

    return render(request,'quora/registration.html',
    		                     {'user_form':user_form,
    		                     'profile_form':profile_form,
    		                     'registered':registered})    

def login_view(request):
    logged_in = False
    userdata = UserFormLogin(data = request.POST or None)
    user = None
    #print("1")
    if request.method == 'POST': 
         #print("2")
         #print("k")
         if userdata.is_valid():
             #print("3")
             username = userdata.cleaned_data.get('username')
             password = userdata.cleaned_data.get('password')
             #print(username)
             user = authenticate(request,username=username,password=password)
             if user:
                if user.is_active:
                      login(request,user)
                else:
                      return HttpResponse("ACCOUNT NOT ACTIVE")      
               # print("hello")
                logged_in = True
             else: 
               # print("hi")
                print("Someone tried to login and failed")
                print("Username: {} and password {}".format(username,password))
                return HttpResponse("invalid login details supplied!")    
    return render(request,'quora/login.html',{'user_data':user,'logged_in':logged_in,'user_entry':userdata})
   