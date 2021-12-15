from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def statistics(request):
    return render(request, 'statistics.html')

def improvement(request):
    return render(request, 'improvement.html')

def about(request):
    return render(request, 'about.html')

def regist(request):
    return render(request, 'regist.html')

def example(request):
    return render(request, 'example.html')

def example_1(request):
    return render(request, 'example_1.html')