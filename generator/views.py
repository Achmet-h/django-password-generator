from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnop')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDDEFJHIGKLMNOP'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length'))

    definitive_pas = ''
    for x in range(length):
        definitive_pas += random.choice(characters)

    return render(request, 'generator/password.html', {'password': definitive_pas})

def overus(request):
    return render(request, 'generator/overus.html')