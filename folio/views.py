from django.shortcuts import render, HttpResponse

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    return render(request, 'home.html')

def education(request):   
    return render(request,'education.html')

def about(request):    
    return render(request,'about.html')

def contacts(request):   
    return render(request,'contacts us.html')
