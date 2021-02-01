from django.shortcuts import render, redirect, HttpResponse
from .models import tvShow, Network

def index(request):
    return redirect('/shows/new')

def shows(request):
    context = {
        'allShows' : tvShow.objects.all(),
        'allNetworks': Network.objects.all()
    }
    return render(request, 'showIndex.html', context)

def newShow(request):
    context = {
        'allNetworks': Network.objects.all()
    }    
    return render(request, 'addShow.html', context)

def createShow(request):
    newNetwork = Network.objects.get(id = request.POST['network'])
    newShow = tvShow.objects.create(
        title = request.POST['title'],
        reDate = request.POST['reDate'],
        desc = request.POST['desc']
    )
    id = newShow.id
    newShow.networks.add(newNetwork)
    return redirect(f'/shows/{id}')

def showDetail(request, id):
    thisShow = tvShow.objects.get(id = id)
    context = {
        'show': thisShow
    }
    return render(request,'showInfo.html',context)

def editShow(request, id):
    context = {
        'show' : tvShow.objects.get(id = id),
        'allShows' : tvShow.objects.all(),
        'allNetworks': Network.objects.all()
    }
    print(id)
    
    return render(request,'editShow.html',context)

def updateShow(request, id):
    updateShow = tvShow.objects.get(id = id)
    updateShow.title = request.POST['title']
    
    updateShow.reDate = request.POST['reDate']
    updateShow.desc = request.POST['desc']
    
    updateShow.save()
    updateShow.networks.add(Network.objects.get(id = request.POST['network']))
    print(id)
    print(updateShow.networks.last().name)
    return redirect(f'/shows/{id}')

# def addNetwork(request):
#     thisNet = Network.objects.get(id = request.POST ['network'])
#     thisShow = tvShow.objects.get(id = request.POST ['show.id'])
#     thisShow.networks.add(thisNet)
#     return redirect(f'/shows/{id}')

def destroyShow(request, id):
    deleteShow = tvShow.objects.get(id = id)
    deleteShow.delete()
    return redirect('/shows')

