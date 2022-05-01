from multiprocessing import context
from django.shortcuts import render  # ດຶງມາຈາກ template
from django.http import HttpResponse  # ຂຽນເທິງກະດານ
from .models import ExamScore

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

def ShowScore(request) :
     #return HttpResponse('Persons Page')
     score = ExamScore.objects.all() #ດຶງຄ່າມາຈາກ Database ທັງໝົດ
     context = {'score':score}
     return render(request, 'school/showscore.html', context)