from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello.html')

def test(request):
    return render(request, 'test.html')

def info(request):
    return render(request, 'info.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
