from django.shortcuts import render,HttpResponse, redirect

def index(request):
    return render(request,'dojo_index.html')

def processing(request):
    print(request.POST)
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comments = request.POST['comments']

    return redirect(f'/results/{name}/{location}/{language}/{comments}')

def results(request, name, location, language, comments):
    context = {
        'name' : name,
        'location' : location,
        'language' : language,
        'comments' : comments,
    }
    return render(request, "dojo_return.html", context)