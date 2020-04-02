from django.shortcuts import render


def login(request):
    """Return the login.html file"""
    return render(request, 'login.html')
