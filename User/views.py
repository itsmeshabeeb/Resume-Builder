from django.shortcuts import render
from django.http import HttpResponse  

# Create your views here.
def into(request):
    return HttpResponse('you are a User')