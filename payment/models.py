from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование товара",
        help_text='Наименование товара'
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание",
        help_text="Описание товара"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость',
        help_text="Стоимость выбранного товара",
    )
    icon = models.ImageField(
        blank=True,
        upload_to='product_icons'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'item_id': self.pk})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания заказа")
    date_change = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения заказа")
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Заказчик'
    )
    items = models.ManyToManyField(
        Item,
        blank=True,
        related_name="ord"
    )

    def __str__(self):
        return f'Номер заказа № {self.pk}'

    def get_count(self):
        count = self.items.count()
        return count

    def get_price(self):
        total_price = 0
        for item in list(self.items.all()):
            total_price += item.price
        print(total_price)
        return total_price

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


# class Discount(models.Model):
#     name = models.CharField(
#         unique=True,
#         max_length=255,
#         verbose_name="Наименование дисконтного предложения",
#         help_text='Наименование дисконтного предложения'
#     )
#     value = models.DecimalField(
#         max_digits=2,
#         decimal_places=2,
#         verbose_name='Скидка',
#         help_text="Размер предлагаемой скидки",
#     )
#     date_create = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Дата создания дисконтного предложения")
#     date_change = models.DateTimeField(
#         auto_now=True,
#         verbose_name="Дата и время дисконтного предложения")
#
#     def __str__(self):
#         return self.name
#