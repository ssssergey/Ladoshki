# -*- coding: utf-8 -*-
from django import template
import locale

register = template.Library()


@register.filter(name=u'currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL, '')
    loc = locale.localeconv()
    return locale.currency(value, loc['currency_symbol'], grouping=False)
