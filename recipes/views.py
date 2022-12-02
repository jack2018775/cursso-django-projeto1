from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html',{'nome':'jackson cavalcante da silva'})



# Create your views here.
