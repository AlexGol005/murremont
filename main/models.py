from decimal import Decimal
from django.db import models

STATUS = (
        ('Новый', 'Новый'),
        ('Обсуждаем', 'Обсуждаем'),
        ('Ждет выезда', 'Ждет выезда'),
        ('Выполнен', 'Выполнен'),
        ('Отказ до', 'Отказ до'),
        ('Отказ после', 'Отказ после'),
    )
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
    term = models.DecimalField('Срок, часов', max_digits=2, decimal_places=0, default='', blank=True, null=True)
    price = models.DecimalField('Стоимость', max_digits=9, decimal_places=2, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if self.term <= Decimal(3):
    #         self.price = self.term * Decimal(1500)
    #     if Decimal(8) > self.term > Decimal(3):
    #         self.price = (self.term - Decimal(3)) * Decimal(800) + Decimal(4500)
    #     if self.term == Decimal(8):
    #         self.price = Decimal(8100)
    #     if self.term > Decimal(8):
    #         self.price = (self.term / Decimal(8)) * 8100
    #     super(Repair, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.name} цена {self.price}'

    class Meta:
        verbose_name = 'Прайс работ'
        verbose_name_plural = 'Прайс работ'

class Order(models.Model):
    person = models.CharField('имя', max_length=100)
    adress = models.CharField('адрес', max_length=1000, blank=True, null=True)
    repair = models.CharField('работы по прайсу', max_length=1000, blank=True, null=True)
    comment = models.TextField('комментарий', max_length=1000, blank=True, null=True)
    telephone = models.CharField('телефон', max_length=12, blank=True, null=True)
    email = models.CharField('email', max_length=100, blank=True, null=True)
    status = models.CharField(max_length=300, choices=STATUS, default='Новый', null=True,
                              verbose_name='Статус')
    commentmanager = models.TextField('комментарий менеджера', max_length=1000, blank=True, null=True)


    def __str__(self):
        return f'{self.person} ,  {self.telephone}, {self.repair}, {self.adress}, ст: {self.status}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
