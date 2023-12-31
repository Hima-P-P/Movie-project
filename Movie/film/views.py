
from django.shortcuts import render
from film.models import Film
from film.forms import movieform

# def home(request):
#     return render(request,'home.html')
def addmovie(request):
    return render(request,'addmovie.html')

def view(request):
    return render(request,'view.html')

def home(request):
    b=Film.objects.all()
    return render(request,'home.html',{'films':b})
def addmovie(request):
    if(request.method=="POST"):
        n=request.POST['n']
        d=request.POST['d']
        y=request.POST['y']
        i=request.FILES['i']
        b=Film.objects.create(name=n,desc=d,year=y,image=i)
        b.save()
        return home(request)
    return render(request,'addmovie.html')
def viewmovie(request,p):
    b=Film.objects.get(id=p)
    return render(request,'view.html',{'films':b})

def deletemovie(request,p):
    b=Film.objects.get(id=p)
    b.delete()
    return home(request)

def updatemovie(request,p):  #builtin form
    b=Film.objects.get(id=p)
    form=movieform(instance=b)
    if(request.method=="POST"):
        form=movieform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'update.html',{'form':form})

