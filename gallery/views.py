from django.shortcuts import render


def gallery(request):
    """Return the gallery.html file"""
    return render(request, 'gallery.html')
