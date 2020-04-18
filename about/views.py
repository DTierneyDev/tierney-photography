from django.shortcuts import render


def about(request):
    """Return the about.html file"""
    return render(request, 'about.html')
