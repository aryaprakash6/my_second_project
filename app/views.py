from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def arya(request):
    return HttpResponse('<h1><marquee>Hellooooo</h1></marquee>')
def preethi(request):
    return HttpResponse('<h1><marquee>Preethi okaManchi Ammayiii</h1></marquee>')
