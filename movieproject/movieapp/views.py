from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):

    movie=Movie.objects.all()


    return render(request,"index.html",{'variable':movie})

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'variable2':movie})


def add(request):

    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        image=request.FILES['image']

        movie=Movie(name=name,desc=desc,year=year,image=image)
        movie.save()
    return render(request,"add.html")

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')