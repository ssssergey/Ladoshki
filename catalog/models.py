# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.db import models





class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(u'Название категории', max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    description = models.TextField(u'Описание категории')
    is_active = models.BooleanField(u'Активна', default=True)
    meta_keywords = models.CharField(u'Мета ключевые слова', max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(u'Мета описание', max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(u'Создана', auto_now_add=True)
    updated_at = models.DateTimeField(u'Изменена', auto_now=True)
    objects = models.Manager()
    active = ActiveCategoryManager()

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_category', args=(self.slug,))

    def get_absolute_url_boys(self):
        return reverse('catalog_category', args=(self.slug, u'boy'))

    def get_absolute_url_girls(self):
        return reverse('catalog_category', args=(self.slug, u'girl'))


class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all().filter(is_active=True).filter(is_featured=True)

class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(is_active=True)

class Product(models.Model):
    GENDER_CHOICE = (
        ('BOY', u'Мальчик'),
        ('GIRL', u'Девочка'),
        ('UNI', u'Унисекс'),
    )

    name = models.CharField(u'Название товара', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    gender = models.CharField(u'Пол', max_length=4, choices=GENDER_CHOICE, default='BOY')
    brand = models.CharField(u'Фирма-производитель', max_length=50, blank=True)
    country = models.CharField(u'Страна-производитель', max_length=50, blank=True)
    color = models.CharField(u'Цвет', max_length=50, blank=True)
    sizes = models.CharField(u'Размеры', max_length=100, default='0')
    categories = models.ManyToManyField(Category, verbose_name=u'Категории')
    price = models.IntegerField(u'Цена')
    old_price = models.IntegerField(u'Старая цена', default=0)
    is_active = models.BooleanField(u'В наличии', default=True)
    is_bestseller = models.BooleanField(u'Хит продаж', default=False)
    is_featured = models.BooleanField(u'Спецпредложение', default=False)
    quantity = models.IntegerField(u'Количество', default=1)
    description = models.TextField(u'Описание')
    meta_keywords = models.CharField(u'Мета ключевые слова', max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(u'Мета описание', max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(u'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(u'Изменен', auto_now=True)
    image = models.ImageField(u'Большое фото', upload_to='images/products/main')
    thumbnail = models.ImageField(u'Малое фото', upload_to='images/products/thumbnails')
    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args=(self.slug,))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


class ActiveProductReviewManager(models.Manager):
    def all(self):
        return super(ActiveProductReviewManager, self).all().filter(is_approved=True)


class ProductReview(models.Model):
    RATINGS = ((5, 5), (4, 4), (3, 3), (2, 2), (1, 1),)

    product = models.ForeignKey(Product, verbose_name=u'Товар')
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    date = models.DateTimeField(u'Создан', auto_now_add=True)
    rating = models.PositiveSmallIntegerField(u'Рейтинг', default=5, choices=RATINGS)
    is_approved = models.BooleanField(u'Одобрен', default=True)
    content = models.TextField(u'Текст')
    objects = models.Manager()
    approved = ActiveProductReviewManager()
