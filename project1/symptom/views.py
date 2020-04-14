from django.shortcuts import render
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from symptom.models import contact

# Encryption libraries required for
# getting token before each api request
import base64
import hashlib,hmac

# api request library
import requests


'''
This is the most important file , please check and maintain this before anything
else. Please try to mention my name in contributors section in your project ,
...just kidding.
btw my name's abhishek.
'''


def index(request):
    return render(request,'index.html')

def covid(request):
    return render(request,'covid19.html')

def contact1(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname','')
        last_name=request.POST.get('lastname','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        feedback=request.POST.get('feedback','')
        contact1=contact(contact_first=first_name,contact_last=last_name,contact_email=email,contact_subject=subject,contact_feedback=feedback)
        contact1.save()
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('index.html')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index.html')

def registration(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['cpassword']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('registration.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('registration.html')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                return redirect('login.html')
        else:
            messages.info(request,"password doesnot match")
            return redirect('registration.html')
    else:
        return render(request,'registration.html')


#Call this function each time before making api request and pass it in the request url
# E.x : https://sandbox-healthservice.priaid.ch/symptoms?token=  <--this is where you need your token.

def create_token():
    # your apimedic credentials's username
    username="My_Username_here"
    # your apimedic credentials's password 
    password="My_password_here"

    #Don't change this !
    req_uri='https://sandbox-authservice.priaid.ch/login'

    #some encryption for making a post request , to ask for token from apimedic
    raw_hash=hmac.new(password.encode("utf-8"),req_uri.encode("utf-8"),hashlib.md5)
    computed_hash=base64.b64encode(raw_hash.digest())

    header={
        'Authorization': f"Bearer {username}:{computed_hash.decode('utf-8')}",
    }

    myreq=requests.post(req_uri,headers=header)
    response=myreq.json()

    #check your cmd window , this is your api token 
    #you need to create this each time before making
    #request to apimedic
    print(response['Token'])

    return response['Token']


'''
Parameter 	    Type 	Values

symptoms 	    JSON    encoded int[] array 	Serialized array of selected symptom ids in json format. example symptoms=[234,235,236]

gender 	        string 	male, female

year_of_birth 	int 	

'''
def my_diagnosis(symptoms,gender,year_of_birth):
    token=create_token()
    # This is how you make a api call/request
    response=requests.get('https://sandbox-healthservice.priaid.ch/diagnosis',token=token,language='en-gb',symptoms=symptoms,gender=gender,year_of_birth=year_of_birth)
    # if status_code == 200 then be happy else google the http status_codes
    print(response.status_code)
    return response.json()