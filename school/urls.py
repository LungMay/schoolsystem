from django.urls import path
from .views import *
urlpatterns = [
    #localhost:8000/
    path('', HomePage, name="home-page"),
    #localhost:8000/about
    path('about/', AboutPage, name='about-page'),
    #localhost:8000/contact
    path('contact/', ContactPage, name='contact-page'),
    #localhost:8000/score
    path('score/', ShowScore, name='score-page')
]