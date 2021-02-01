from django.shortcuts import render, HttpResponse
from time import localtime, strftime
    
def index(request):
    context = {
        "time": strftime("%B %d %Y", localtime()),
        "time2": strftime("%H:%M %p", localtime())
    }
    return render(request,'time_index.html', context)