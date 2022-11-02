from decimal import Decimal

from django.db import models

class Type(models.Model):
    name = models.CharField('Тип работ', max_length=100, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип работ'
        verbose_name_plural = 'Тип работ'


class Repair(models.Model):
    type = models.ForeignKey(Type, verbose_name='тип', on_delete=models.SET_NULL, null=True)
    name = models.CharField('Название', max_length=100, unique=True)
    term = models.DecimalField('Срок, часов', max_digits=2, decimal_places=0, default='1', blank=True)
    price = models.DecimalField('Стоимость', max_digits=9, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        if self.term <= Decimal(7):
            self.price = (self.term - Decimal(1)) * Decimal(600) + Decimal(1000)
        if self.term == Decimal(8):
            self.price = Decimal(5000)
        if self.term > Decimal(8):
            self.price = (self.term / Decimal(8)) * 5000


    def __str__(self):
        return f'{self.name} цена {self.price}'

    class Meta:
        verbose_name = 'Прайс работ'
        verbose_name_plural = 'Прайс работ'
