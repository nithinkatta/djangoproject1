from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'temp.html')

def signup(request):
    return render(request,'signup.html')

def submit(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    password = request.GET['pass']
    rpass = request.GET['rpass']
    email = request.GET['email']
    add = request.GET['add']
    if password != rpass or fname=='' or lname=='' or password=='' or rpass=='':
        return render(request,'signup.html')
    else:
        return render(request,'result.html',{'name': fname, 'lname':lname,'pass':password,'rpass':rpass,'email':email,'add':add})