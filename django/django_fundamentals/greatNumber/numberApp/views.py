from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'num' not in request.session:
        request.session['num'] = random.randint(1, 100)
    print(request.session['num'])

    return render(request,'numbersIndex.html')

def guess(request):
    userGuess = int(request.POST['userGuess'])
    serverNum = request.session['num']
    clue = ''
    if serverNum > userGuess:
        clue = 'Too Low'
        
    elif serverNum < userGuess:
        clue = 'Too High'
        
    else:
        clue = 'Correct'
        request.session['clue'] = clue
        return redirect('/correct')

    request.session['clue'] = clue
    print(request.session['clue'])
    return redirect('/')

def correct(request):
    return render(request,'correctIndex.html')

def playAgain(request):
    request.session.clear()
    return redirect('/')