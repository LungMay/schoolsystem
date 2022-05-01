from django.shortcuts import render  # ດຶງມາຈາກ template
from django.http import HttpResponse  # ຂຽນເທິງກະດານ

# Create your views here.
def HomePage(request) :
     # return HttpResponse('<h1>Home Page</h1>')
     return render(request, 'school/home.html')

def AboutPage(request) :
     #return HttpResponse('About Page')
     return render(request, 'school/about.html')

def ContactPage(request) :
     #return HttpResponse('Contact Page')
     return render(request, 'school/contact.html')

#def persons(request) :
 #   return HttpResponse('Persons Page')