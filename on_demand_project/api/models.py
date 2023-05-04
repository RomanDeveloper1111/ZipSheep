from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage


class Courier(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Awesome'),
        (5, 'Excellent')
    )

    fio = models.CharField(max_length=100, verbose_name="FIO")
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    phone_number = models.CharField(max_length=15)


class Client(models.Model):
    fio = models.CharField(max_length=100, verbose_name="FIO")
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Currency(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name_plural = "Currency"


class Invoice(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    order_location = models.CharField(max_length=500, null=False)
    destination_address = models.CharField(max_length=100)
    duration = models.TimeField(null=True)
    weight_order = models.DecimalField(decimal_places=2, max_digits=4)
    time_accept = models.DateTimeField(auto_now_add=True)
    time_done = models.DateTimeField()
    tips = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)


@receiver(post_save, sender=Currency)
def post_save_dispatcher(sender, instance, created, *args, **kwargs):
    if created:
        recipient_list = ['ignatenko-roma@list.ru', ]
        msg = EmailMessage(subject='On demand project', body='A new currency have been added!', to=recipient_list)
        msg.send()
        print(f'Курс валюты был создан: {instance.name}')
