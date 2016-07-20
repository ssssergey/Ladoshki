# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import cart


def show_cart(request, template_name="cart/cart.html"):
    cart_item_count = cart.cart_item_count(request)
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == u'Удалить':
            cart.remove_from_cart(request)
        if postdata['submit'] == u'Сохранить':
            cart.update_cart(request)
    cart_items = cart.get_cart_items(request)
    page_title = u'Корзина'
    cart_subtotal = cart.cart_subtotal(request)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

