from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"login.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')

    password = request.POST['password']
    hashBrowns = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    newUser = User.objects.create(
        fname = request.POST ['fname'],
        lname = request.POST ['lname'],
        email = request.POST ['email'],
        password = hashBrowns
    )
    request.session['user_id'] = newUser.id
    return redirect ('/success')

def logIn(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')
    userList = User.objects.filter(email = request.POST['email'])
    if userList:
        ourUser = userList[0]
        if bcrypt.checkpw(request.POST['password'].encode(), ourUser.password.encode()):
            print('passwords match')
            request.session['user_id'] = ourUser.id
            return redirect('/success')
    else:
        print('No User found')
        messages.error(request,'User not found, or incorrect password.')
    return ('/')

def success(request):
    # print(request.session['user_id'])
    logged_in_user = User.objects.get(id = request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user
    }
    return render(request,'success.html',context)

def logOut(request):
    request.session.flush()
    return redirect('/')