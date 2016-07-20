from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^confirm/$', confirm_order, {'template_name': 'ordering/confirm.html'}, 'confirm_order'),
    url(r'^send_email/$', send_email, {'template_name': 'ordering/thanks.html'}, 'send_email'),
]
