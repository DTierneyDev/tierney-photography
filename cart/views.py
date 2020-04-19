from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request):
    """Renders the cart contents page"""
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """Add a photoset to the cart"""

    cart = request.session.get('cart', {})

    if id not in cart.keys():
        cart[id] = cart.get(id)

    request.session['cart'] = cart
    messages.error(request, "Item added to your cart!")
    return redirect(reverse('shop'))


def remove_from_cart(request, id):
    """Remove a photoset from the cart"""
    cart = request.session.get('cart', {})

    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
