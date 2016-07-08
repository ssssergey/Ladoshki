# -*- coding: utf-8 -*-

from forms import RegisterForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect


def register(request, template_name="registration/register.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = RegisterForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username', '')
            pw = postdata.get('password1', '')
            from django.contrib.auth import login, authenticate

            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = urlresolvers.reverse('catalog_home')
                return HttpResponseRedirect(url)
    else:
        form = RegisterForm()
    page_title = u'Регистрация пользователя'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

# from checkout.models import Order, OrderItem
# from django.contrib.auth.decorators import login_required
# @login_required
# def my_account(request, template_name="registration/my_account.html"):
#     page_title = 'My Account'
#     orders = Order.objects.filter(user=request.user)
#     name = request.user.username
#     return render_to_response(template_name, locals(),context_instance=RequestContext(request))