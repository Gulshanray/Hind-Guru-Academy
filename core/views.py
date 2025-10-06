from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def destinations(request):
    return render(request, 'destinations.html')

def scholarships(request):
    return render(request, 'scholarships.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')
