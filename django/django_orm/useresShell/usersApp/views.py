from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse('IT HAS BEGUN!!!')