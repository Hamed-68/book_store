from django.db import models
from decimal import Decimal


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام کتاب')
    author = models.CharField(max_length=200, verbose_name='نویسنده')
    genre = models.CharField(max_length=200, verbose_name='ژانر')
    inventory = models.PositiveIntegerField(default=1, verbose_name='موجودی')
    price = models.DecimalField(decimal_places=0, max_digits=20, verbose_name='قیمت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ افزودن کتاب')
    products = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصولات')
    percent_discount = models.FloatField(default=0, verbose_name='تخفیف درصدی')

    class Meta:
        ordering = ['name']

    def get_price(self):
        p = self.price - (self.price * Decimal(self.percent_discount))
        return round(p)

    def __str__(self):
        return self.name
