from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def cake(request):
    return HttpResponse('i like cake')
