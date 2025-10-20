from django.shortcuts import render
from django.http import HttpResponse

def view_kago(request):
    return HttpResponse("Hello Kago")
