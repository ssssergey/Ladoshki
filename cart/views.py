# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site

import cart
from Ladoshki.settings import EMAIL_HOST_USER
from forms import ContactForm


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


def confirm_order(request):
    domain_url = ''.join(['http://', get_current_site(request).domain])
    cart_items = cart.get_cart_items(request)
    page_title = u'Подтверждение'
    cart_item_count = cart.cart_item_count(request)
    cart_subtotal = cart.cart_subtotal(request)
    form = ContactForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            recipients = ['lse1983@mail.ru','Prokidjan@rambler.ru']
            # Send email
            plaintext = get_template('cart/mail.txt')
            htmly = get_template('cart/mail.html')
            d = Context({'cart_items': cart_items, 'cart_item_count': cart_item_count, 'cart_subtotal': cart_subtotal,
                         'phone': phone, 'email': email, 'domain_url': domain_url})
            subject, from_email, to = u'ЗАКАЗ', EMAIL_HOST_USER, recipients
            # text_content = plaintext.render(d)
            html_content = htmly.render(d)
            text_content = render_to_string('cart/mail.html',
                                            {'cart_items': cart_items, 'cart_item_count': cart_item_count,
                                             'cart_subtotal': cart_subtotal,
                                             'phone': phone, 'email': email, 'domain_url': domain_url})
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # Clear Cart
            cart_items.delete()
            page_title = u'Спасибо за заказ!'
            return render_to_response("cart/thanks.html", {'request': request, 'page_title': page_title})
    return render_to_response("cart/confirm.html", locals(), context_instance=RequestContext(request))
