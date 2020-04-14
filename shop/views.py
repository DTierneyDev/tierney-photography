from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import PhotoSet
from .forms import PhotoSetForm


def get_photosets(request):
    """Create a view that will return a list of photosets
    that were published prior to 'now' and render them to 'shop.html'"""

    photosets = PhotoSet.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'shop.html', {'photosets': photosets})


def photoset_detail(request, pk):
    """Create a view that returns a single photoset based on ID (pk)
    and render it to 'shopdetail.html' or return 404 if not found"""

    photoset = get_object_or_404(PhotoSet, pk=pk)
    photoset.save()
    return render(request, 'shopdetail.html', {'photoset': photoset})


def create_or_edit_photoset(request, pk=None):
    """Create a view that allows the admin to create or edit
    a photoset depending on whether the ID is null or not"""

    photoset = get_object_or_404(PhotoSet, pk=pk) if pk else None
    if request.method == "POST":
        form = PhotoSetForm(request.POST, request.FILES, instance=photoset)
        if form.is_valid():
            photoset = form.save()
            return redirect(photoset_detail, photoset.pk)
    else:
        form = PhotoSetForm(instance=photoset)
    return render(request, 'photosetform.html', {'form': form})
