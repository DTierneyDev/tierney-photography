from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """Renders the cart contents page"""
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """Add a photoset to the cart"""
    # quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id)
    
    # if id in cart:
    #     cart[id] = int(cart[id]) + quantity
    # else:
    #     cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    """Remove a photoset from the cart"""
    cart = request.session.get('cart', {})

    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
