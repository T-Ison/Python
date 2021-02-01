from django.shortcuts import render, HttpResponse, redirect
from . models import Book, Author

def index(request):
    return render(request, ('index.html'))