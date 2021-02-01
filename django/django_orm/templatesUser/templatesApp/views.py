from django.shortcuts import render, redirect, HttpResponse
from . models import User

def index(request):
    print(User.objects.all())
    context = {
        'all_users': User.objects.all()
    }
    return render(request,"index.html", context)

def process(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    age = request.POST['age']
    User.objects.create(
        fname=fname, 
        lname=lname, 
        email=email, 
        age=age
        )
    return redirect('/')