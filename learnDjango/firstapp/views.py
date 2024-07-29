from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("Ini adalah halaman test!")

def test_two(request):
    return HttpResponse("Ini Test Ke 2")