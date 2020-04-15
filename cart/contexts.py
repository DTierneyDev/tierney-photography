from django.shortcuts import get_object_or_404
from shop.models import PhotoSet


def cart_contents(request):
    """Makes sure the cart contents are available when rendering every page"""

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    photoset_count = 0
    for id in cart.items():
        photoset = get_object_or_404(PhotoSet, pk=id)
        total += photoset.price
        photoset_count += 1
        cart_items.append({'id': id, 'photoset': photoset})
        
    # for id, quantity in cart.items():
    #     photoset = get_object_or_404(PhotoSet, pk=id)
    #     total += quantity * photoset.price
    #     photoset_count += quantity
    #     cart_items.append({'id': id, 'quantity': quantity, 'photoset': photoset})

    return {'cart_items': cart_items, 'total': total, 'photoset_count': photoset_count}
