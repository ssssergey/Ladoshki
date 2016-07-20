# -*- coding: utf-8 -*-
from django import forms
from catalog.models import Product, ProductReview


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError(u'Цена должна быть положительным числом.')
        return self.cleaned_data['price']


class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={'size': '2', 'value': '1', 'class': 'quantity form-control', 'maxlength': '5'}),
        error_messages={'invalid': u'Введите число.'}, min_value=1, label=u'Количество')
    product_slug = forms.CharField(widget=forms.HiddenInput())
    # override the default __init__ so we can set the request
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    # custom validation to check for cookies
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(u"Включите куки в настройках браузера.")
        return self.cleaned_data


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ('user', 'product', 'is_approved')

    def __init__(self, *args, **kwargs):
        super(ProductReviewForm, self).__init__(*args, **kwargs)
        default_text = u'Ваш отзыв'
        self.fields['content'].widget.attrs['value'] = default_text
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['cols'] = 5
