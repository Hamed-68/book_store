from django.db import models
from decimal import Decimal


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    familly = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    birthday = models.DateField(blank=True, verbose_name='زاد روز')
    country = models.CharField(max_length=200, verbose_name='ملیت')

    def __str__(self):
        return f'{self.name} {self.familly}'


class Genre(models.Model):
    title = models.CharField(max_length=150, verbose_name='ژانر')

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام کتاب')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='نویسنده')
    genre = models.ManyToManyField(Genre, verbose_name='ژانر')
    inventory = models.PositiveIntegerField(default=1, verbose_name='موجودی')
    price = models.DecimalField(decimal_places=0, max_digits=20, verbose_name='قیمت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ افزودن کتاب')
    percent_discount = models.FloatField(default=0, verbose_name='تخفیف درصدی')
    image = models.ImageField(upload_to='images', verbose_name='تصویر', blank=True)

    class Meta:
        ordering = ['created_at']

    def get_price(self):
        p = self.price - (self.price * Decimal(self.percent_discount))
        return round(p)

    def __str__(self):
        return self.title
