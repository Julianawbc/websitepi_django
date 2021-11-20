from django.shortcuts import render    #views são visualizações criadas para o usuario
from django.http import HttpResponse, request

def cadastro(request):
    return render(request, 'cadastro.html')


def login (request):
    return render(request, 'login.html')  
