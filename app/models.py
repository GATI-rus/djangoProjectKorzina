from django.db import models
from django.contrib.auth.models import User


class Tovar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена товара')
    image = models.CharField(max_length=2000, verbose_name='Изображение')
    discount = models.FloatField(default=0, verbose_name='Скидка в %')

    def __str__(self):
        return self.name

class Cart(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество товаров')
    summa = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Сумма товара')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')

    def __str__(self):
        return self.tovar


    def calcSumma(self):
        return self.count * (self.tovar.price - self.tovar.discount / 100 * self.tovar.price)


class Order(models.Model):
    adres = models.CharField(max_length=150, verbose_name='Адрес')
    tel = models.CharField(max_length=12, verbose_name='Номер телефона')
    emil = models.CharField(max_length=50, verbose_name='Почта')
    total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    myzakaz = models.TextField(verbose_name='Заказ')
