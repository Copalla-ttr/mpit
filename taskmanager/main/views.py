from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def what_is(request):
    return render(request, 'main/what_is.html')


def wallet(request):
    return render(request, 'main/wallet.html')


def categories(request):
    return render(request, 'main/categories.html')


def tasks(request):
    return render(request, 'main/tasks.html')

def partners(request):
    return render(request, 'main/partners.html')