from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
  return HttpResponse('Hello')
# Create your views here.
def Home(request):
  return HttpResponse('it is Home')
