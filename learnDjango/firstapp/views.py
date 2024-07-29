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

# form
def create(request):
    return render(request, 'create.html')

from .form import MyForm
from .models import Users

def submit_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            # Ambil Datanya
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            Users.objects.create(name=name, email=email)

            return render(request, 'create.html', {'message':'success'})
    else:
        form = MyForm()

    return render(request, 'form.html', {'message':'Failed', 'form': form})