from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0

    return render(request, "counter_index.html")

def reset_session(request):
    request.session.clear()
    return redirect ('/')