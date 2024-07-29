from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    data = {
        'title': 'Test Page Dinamis',
        'message': 'Ini adalah halaman test.',
        'items': ['Apple', 'Banana', 'Cherry']
    }

    return render(request, 'test.html', data)

def test_two(request):
    return HttpResponse("Ini Test Ke 2")

def home(request):
    return render(request, 'home.html')