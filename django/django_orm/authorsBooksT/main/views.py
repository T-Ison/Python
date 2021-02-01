from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author

def index(request):
    print(Book.objects.all())
    context = {
        'allBooks': Book.objects.all()
    }
    return render(request,"addBook.html", context)

def processBook(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc'],
    )
    return redirect('/')

def bookDetail(request, book_id):
    print(book_id)
    thisBook = Book.objects.get(id = book_id)
    context = {
        'book': thisBook,
        'allAuthors': Author.objects.all()
    }
    return render(request, "bookDetail.html", context)

def addAuthor_toBooks(request):
    thisAuthor = Author.objects.get(id=request.POST['author_id'])
    thisBook = Book.objects.get(id=request.POST['book_id'])
    thisBook.authors.add(thisAuthor)
    return redirect(f'/books/{thisBook.id}')

#  ********************** Authors *****************************

def authors(request):
    print(Author.objects.all())
    context = {
        'allAuthors': Author.objects.all()
    }
    return render(request,"addAuthor.html", context)

def processAuthor(request):
    Author.objects.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        notes=request.POST['notes'],
    )
    return redirect('/authors')

def authorNotes(request, author_id):
    print(author_id)
    thisAuthor = Author.objects.get(id = author_id)
    context = {
        'author': thisAuthor,
        'allBooks': Book.objects.all()
    }
    return render(request, "authorNotes.html", context)

def addBooks_toAuthor(request):
    thisBook = Book.objects.get(id=request.POST['book_id'])
    thisAuthor = Author.objects.get(id=request.POST['author_id'])
    thisAuthor.books.add(thisBook)
    return redirect(f'/authors/{thisAuthor.id}')