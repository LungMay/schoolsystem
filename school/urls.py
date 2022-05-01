from django.urls import path
from .views import HomePage

urlpatterns = [
    #localhost:8000/
    path('', HomePage)
]