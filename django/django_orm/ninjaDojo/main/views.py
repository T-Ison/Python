from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

def index(request):
    print(Dojo.objects.all())
    myDojos = Dojo.objects.all()
    context = {
        'allDojos': Dojo.objects.all(),
        'allNinjas': Ninja.objects.all()
    }
    return render(request,"index.html", context)

def processDojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(
        name=name, 
        city=city, 
        state=state,
        )
    return redirect('/')

def processNinja(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    dojo = request.POST['dojo']
    thisDojo = Dojo.objects.get(id=dojo)
    print(thisDojo)
    Ninja.objects.create(
        fname=fname, 
        lname=lname, 
        dojos=thisDojo
        )
    return redirect('/')