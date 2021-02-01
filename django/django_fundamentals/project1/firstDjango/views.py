from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
        return redirect('/blog')

def index(request):
        return HttpResponse("Blog Page")

def new(request):
        return HttpResponse("Display Blog Page")

def create(request):
        return redirect('/')

def show(request,number):
        return HttpResponse({number})

def edit(request,number):
        return HttpResponse({number})

def destroy(request,number):
        return redirect('/blogs')

def bonus(request):
        return JsonResponse({"response": "JSON response from redirected_method", "status": True})
