from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from requests import request
# Create your views here.


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Elamannnnn'})


def say_azim(request):
    return HttpResponse('hello Azim')
