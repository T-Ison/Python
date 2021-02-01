from django.shortcuts import render, redirect
from .models import User, Post, Comment
from django.contrib import messages
import bcrypt

def dump(obj):
    for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

def index(request):
    return render(request,'login.html')

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

def login(request):
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
    return render(request,'wall.html',context)

def wall(request):
    allUsers = User.objects.first()
    allMessages = Post.objects.all().order_by('created_at')
    allComments = Comment.objects.all()
    context = {
        'allUsers' : allUsers,
        'allMessages': allMessages,
        'allComments': allComments
    }
    return render(request,'wall.html', context)

def postMessage(request):
    userObj = User.objects.get(id=request.session['user_id'])
    thisPost = Post.objects.create(
        message = request.POST['post'],
        userPost = userObj
    )
    return redirect('/wall')

def postComment(request, id):
    userObj = User.objects.get(id=request.session['user_id'])
    postMessage = Post.objects.get(id = id)
    thisComment = Comment.objects.create(
        comment = request.POST['comment'],
        userComment = userObj,
        post = postMessage
    )
    return redirect('/wall')

def deleteMessage(request, id):
    deleteMessage = Post.objects.get(id = id)
    deleteMessage.delete()
    return redirect('/wall')

def logout(request):
    request.session.flush()
    return redirect('/')