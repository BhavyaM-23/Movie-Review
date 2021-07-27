from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request,"Main.html")

def movies(request):
    return render(request,"movies.html")

def shortfilms(request):
    return render(request,"shortfilms.html")

def genres(request):
    return render(request,"genres.html")

def about(request):
    return render(request,"about.html")

def sdreview(request):
    return render(request,"sdreview.html")