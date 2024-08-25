from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello_pintu(request):
    return HttpResponse('hello pintu 2')

def say_hello_world(request):
    return HttpResponse('hello world 2')