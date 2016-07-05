# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseOrderInfo(models.Model):
    class Meta:
        abstract = True

    # contact info
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    # shipping information
    shipping_name = models.CharField(max_length=50)
    shipping_address_1 = models.CharField(max_length=50)
    shipping_address_2 = models.CharField(max_length=50, blank=True)
    shipping_city = models.CharField(max_length=50)
    shipping_state = models.CharField(max_length=2)
    shipping_country = models.CharField(max_length=50)
    shipping_zip = models.CharField(max_length=10)
    # billing information
    billing_name = models.CharField(max_length=50)
    billing_address_1 = models.CharField(max_length=50)
    billing_address_2 = models.CharField(max_length=50, blank=True)
    billing_city = models.CharField(max_length=50)
    billing_state = models.CharField(max_length=2)
    billing_country = models.CharField(max_length=50)
    billing_zip = models.CharField(max_length=10)


class UserProfile(BaseOrderInfo):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return 'User Profile for: ' + self.user.username
