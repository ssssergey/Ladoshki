# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives

from forms import *
from Ladoshki.settings import EMAIL_HOST_USER
from cart import cart


def confirm_order(request, template_name="ordering/confirm.html"):
    cart_items = cart.get_cart_items(request)
    page_title = u'Подтверждение'
    cart_item_count = cart.cart_item_count(request)
    cart_subtotal = cart.cart_subtotal(request)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


# принимать POST запрос с confirm.html с полными данными заказчика (особенно нужен телефон).
# Предполагается, что email уже введен при регистрации аккаунта.
def send_email(request, template_name="ordering/thanks.html"):
    recipients = ['lse1983@mail.ru']
    user = ''
    cart_items = cart.get_cart_items(request)
    cart_item_count = cart.cart_item_count(request)
    cart_subtotal = cart.cart_subtotal(request)

    plaintext = get_template('ordering/mail.txt')
    htmly = get_template('ordering/mail.html')
    d = Context({'cart_items': cart_items, 'cart_item_count': cart_item_count, 'cart_subtotal': cart_subtotal})
    subject, from_email, to = u'ЗАКАЗ', EMAIL_HOST_USER, recipients
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # message = render_to_string("ordering/mail.html", {'cart_items': cart_items, 'cart_item_count': cart_item_count,
    #                                                   'cart_subtotal': cart_subtotal})
    # try:
    #     send_mail(u'ЗАКАЗ', message, EMAIL_HOST_USER, recipients)
    # except BadHeaderError:  # Защита от уязвимости
    #     return HttpResponse('Invalid header found')
    page_title = u'Спасибо за заказ!'
    return render_to_response(template_name, {page_title: page_title})

# def contactView(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         # Если форма заполнена корректно, сохраняем все введённые пользователем значения
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             sender = form.cleaned_data['sender']
#             message = form.cleaned_data['message']
#
#             recipients = ['lse1983@mail.ru']
#
#             try:
#                 send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
#             except BadHeaderError:  # Защита от уязвимости
#                 return HttpResponse('Invalid header found')
#                 # Переходим на другую страницу, если сообщение отправлено
#             return render(request, 'site/thanks.html')
#     else:
#         # Заполняем форму
#         form = ContactForm()
#         # Отправляем форму на страницу
#     return render(request, 'site/contact.html', {'form': form})
