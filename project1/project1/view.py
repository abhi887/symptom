import datetime   #from datetime import datetime--------datetime.now()
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from symptom.models import contact,diagnose

def welcome(request):
    now=datetime.datetime.now()
    text="<html><body><h1>hello,this is my first demo</h1><br><h4>Its %s </h4></body></html>" %now
    return HttpResponse(text)
def index(request):
    return render(request,'index.html')
def covid(request):
    return render(request,'covid19.html')
def treatment(request):
    return render(request,'treatment.html')
def symptoms(request):
    return render(request,'symptoms.html')
def prevention(request):
    return render(request,'prevention.html')
def selectsymptom(request):
    return render(request,'selectsymptom.html')
def basic(request):
    return render(request,'basic.html')


def diagnose1(request):
    if request.method=='POST':
        age=request.POST.get('age','')
        gender=request.POST.get('gender','')
        gender1=diagnose(diagnose_age=age,diagnose_gender=gender)
        gender1.save()
        return render(request,'selectsymptom.html')
    else:
        return render(request,'diagnoseme.html')


def about(request):
    return render(request,'about.html')

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
                user.save();
                print("user created")
                return redirect('login.html')
        else:
            messages.info(request,"password doesnot match")
            return redirect('registration.html')
    else:
        return render(request,'registration.html')
