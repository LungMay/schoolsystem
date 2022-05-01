from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomePage(request) :
    return HttpResponse('<h1>Home Page</h1>')

#def about(request) :
 #   return HttpResponse('About Page')

#def contact(request) :
 #   return HttpResponse('Contact Page')

#def persons(request) :
 #   return HttpResponse('Persons Page')