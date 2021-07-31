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

def janatharev(request):
    return render(request,"janatharev.html")

def dhoni(request):
    return render(request,"dhoni.html")

def gully(request):
    return render(request,"gully.html")

def avrev(request):
    return render(request,"avrev.html")

def narappa(request):
    return render(request,"narappa.html")

def action(request):
    return render(request,"action.html")

def drama(request):
    return render(request,"drama.html")

def horror(request):
    return render(request,"horror.html")