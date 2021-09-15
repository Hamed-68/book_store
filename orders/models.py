from django.db import models
from django.conf import settings
from products.models import Book
from django.contrib.humanize.templatetags.humanize import apnumber
from decimal import Decimal


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, verbose_name='مشتری')
    status = models.BooleanField(default=False, verbose_name='وضعیت سفارش')

    def total_price(self):
        total = 0
        for item in self.orderitem_set.all():
            total += item.price_order()
        return total

    def __str__(self):
        return f'سفارش {self.user}'
# ========================================OrderItem=============================


class OrderItem(models.Model):
    CASH = 'CA'
    LOAN_10 = 'L1'
    LOAN_20 = 'L2'
    choice_list = [
        (CASH, 'نقدی'), (LOAN_10, 'نسیه 10 روزه'), (LOAN_20, 'نسیه 20 روزه')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, verbose_name='مشتری')
    product = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='کالا')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    status = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    cash_discount = models.CharField(
        choices=choice_list, max_length=2, default=CASH, verbose_name='تخفیف پرداخت')

    def price_order(self):    # finally price for orderitem
        total = self.product.get_price()
        if self.cash_discount == 'LOAN_10':
            p = (total - (total * 0.05)) * self.quantity
            return p
        elif self.cash_discount == 'LOAN_20':
            p = total * self.quantity
            return p
        p = (total - (total * 0.10)) * self.quantity
        return round(p)

    def __str__(self):
        str_quantity = apnumber(self.quantity)
        return f'{self.product.name} {str_quantity} جلد'
# ========================================PointDiscount=============================


class PointDiscount(models.Model):
    code = models.CharField(max_length=100, verbose_name='کد تخفیف')
    percent = models.FloatField(max_length=10, default=0.0, verbose_name='درصد تخفیف')
