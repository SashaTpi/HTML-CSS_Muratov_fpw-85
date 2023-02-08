from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')

def links(request):
    return render(request, 'main/links.html')

