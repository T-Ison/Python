from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'moneyBag' not in request.session:
        request.session['moneyBag'] = 0
    if 'activityLog' not in request.session:
        request.session['activityLog'] = []
    return render(request,'ninjaIndex.html')

def process(request):
    gold = 0
    message = ''
    if request.POST['choice'] == "farm":
        gold = random.randint(10,20)
        message = f'Earned {gold} from the farm!'
    elif request.POST['choice'] == "cave":
        gold = random.randint(5,10)
        message = f'Earned {gold} from the farm!'
    elif request.POST['choice'] == "house":
        gold = random.randint(2,5)
        message = f'Earned {gold} from the farm!'
    else:
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            gold += random.randint(0,50)
            
        else:
            gold -= random.randint(0,50)
        
        message = f'Earned {gold} from the farm!'
        request.POST['choice'] == "casino"
        
    request.session['activityLog'].append(message)
    request.session['moneyBag'] += gold
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')