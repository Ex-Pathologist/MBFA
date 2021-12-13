from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def statistics(request):
    return render(request, 'statistics.html')

def improvement(request):
    return render(request, 'improvement.html')

def about(request):
    return render(request, 'about.html')
