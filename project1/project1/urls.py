"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

import symptom
from project1 import view

urlpatterns = [
    path('admin/',admin.site.urls),
    url('index',view.index,name='index'),
    url('login',view.login,name='login'),
    url('registration',view.registration,name='registration'),
    url('logout',view.logout,name='logout'),
    url('contact',view.contact1,name='contact'),
    url('covid19',view.covid,name='covid'),
    url('prevention',view.prevention,name='prevention'),
    url('treatment',view.treatment,name='treatment'),
    url('symptoms',view.symptoms,name='symptoms'),
    url('about',view.about,name='about'),
    url('diagnoseme',view.diagnose1,name='diagnose'),
    url('selectsymptom',view.selectsymptom,name='selectsymptom'),

    url('basic',view.basic,name='basic'),








]
