from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

# Create your views here.
def index (request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "date1": strftime("%b %d, %Y", gmtime()),
        "time1": strftime("%I:%M %p",gmtime()),
        "date2": strftime("%A, %B %w, %Y",localtime()),
        "time2":strftime("%H:%M",localtime())
    }
    return render(request,'index.html', context)

def redirigir(request):
    return redirect('/time_display')