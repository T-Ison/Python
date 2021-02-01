from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'index.html')

def processing(request):
    print(request.POST)
    name = request.POST['name']
    age = request.POST['age']
    email = request.POST['email']
    password = request.POST['password']

    return redirect(f'/prt2/{name}/{age}/{email}/{password}')

def prt2(request, name, age, email, password):
    context = {
        'name' : name,
        'age' : age,
        'email' : email,
        'password' : password
    }
    return render(request, "prt2.html", context)