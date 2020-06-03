from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from app.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
        return render(request,"index.html")

def signup(request):
        if request.method == 'POST':
                # *Get the post parameters
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                gender = request.POST['gender']
                city = request.POST['city']
                country = request.POST['country']
                psw = request.POST['psw']
                rpsw = request.POST['rpsw']
                # ? check for errorneous inputs
                #
                if psw != rpsw:
                        messages.error(request,"Please fill correct password!")
                else:
                        user = User(fname=fname,lname=lname,email=email,gender=gender,city=city,country=country,password=psw)
                        user.save()
                        messages.success(request,"Your account is created successfully!")

        return render(request,"signup.html")

def login(request):
        if request.method == 'POST':
                # *Get the post parameters
                loginUsername = request.POST['uname']
                loginPassword = request.POST['pwd']
                # user = authenticate(request,username=loginUsername,password=loginPassword)

                # if user is not None:
                #         login(request,user)
                #         messages.success(request,"Successfully Logged In")
                #         return redirect('Home')
                # else:
                #         messages.success(request,"Invalid Credentials, Please try again")

        return render(request,"login.html")

def myprofile(request):
        return render(request,"myprofile.html")

def about(request):
        return render(request,"about.html")

def contact(request):
        return HttpResponse("Contact Us")
 
def tracker(request):
        return HttpResponse("Tracking")

def search(request):
        return HttpResponse("Search")

def productView(request):
        return render(request,"productview.html")

def checkout(request):
        return HttpResponse("Checkout")

