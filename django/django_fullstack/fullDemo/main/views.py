from django.shortcuts import render, redirect
from .models import User, Author, Book, Review
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
        name = request.POST ['name'],
        alias = request.POST ['alias'],
        email = request.POST ['email'],
        password = hashBrowns
    )
    request.session['user_id'] = newUser.id
    return redirect ('/books')

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
            return redirect('/books')
    else:
        print('No User found')
        messages.error(request,'User not found, or incorrect password.')
    return ('/')

def books(request):
    all_reviews = Review.objects.all()
    latest_reviews = []
    for i in range(len(all_reviews)-1, len(all_reviews)-4, -1):
        latest_reviews.append(all_reviews[i])
    logged_in_user = User.objects.get(id = request.session['user_id'])
    context = {
        'all_books' : Book.objects.all(),
        'logged_in_user': logged_in_user,
        'latest_reviews' : latest_reviews
    }
    return render(request,'books.html',context)

def add_book(request):
    context = {
        'all_authors' : Author.objects.all()
    }
    return render(request, 'add_book.html', context)

def add_book_and_review(request):
    if len(request.POST['new_author']) == 0:
        my_author = Author.objects.get(id = request.POST['existing_author'])
    else:
        my_author = Author.objects.create(name=request.POST['new_author'])
    logged_in_user = User.objects.get(id=request.session['user_id'])
    new_book = Book.objects.create(
        title = request.POST['title'],
        author = my_author,
        submitter = logged_in_user
    )
    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        reviewer = logged_in_user,
        book = new_book
    )
    return redirect('/books')

def book_info(request, book_id):
    context = {
        'book': Book.objects.get(id = book_id)
    }
    return render(request, 'book_info.html',context)

def add_review(request):
    my_book = Book.objects.get(id = request.POST['book_id'])
    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        book = my_book, 
        # getting the book_id from line 31 of book_info.html passing the id behind the scenes
        reviewer = User.objects.get(id = request.session['user_id'])
    )
    return redirect(f'/books/{my_book.id}')

def user_info(request, user_id):
    user = User.objects.get(id = user_id)
    unique_book = []
    for review in user.submitted_reviews.all():
        if review.book.title not in unique_book:
            unique_book.append(review.book)
            
    context ={
        'user': User.objects.get(id = user_id)
    }
    return render(request,'user_info.html',context)

def logOut(request):
    request.session.flush()
    return redirect('/')