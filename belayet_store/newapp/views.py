from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculation():
    x = 2
    y = 6

    return x

def hello(request):
    x = calculation()

    return render(request,'hello.html', {'name':'Hossain'})
