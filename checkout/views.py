from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from shop.models import PhotoSet
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    """ Renders checkout page with forms, if posted tries to process the order and shows errors if there are issues """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id in cart.keys():
                photoset = get_object_or_404(PhotoSet, pk=id)
                total += photoset.price
                order_line_item = OrderLineItem(
                    order=order,
                    photoset=photoset
                )
                order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "Your purchase has been completed! Photosets are now available in your account")
                request.session['cart'] = {}
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        if request.session.get('cart', {}) == {}:
            messages.error(request, "You cannot checkout with no items in the cart")
            return redirect(reverse('view_cart'))
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm(initial={'user': request.user.id})

    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
