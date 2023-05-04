from django.contrib import admin
from .models import Invoice, Currency, Client, Courier


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('price', 'destination_address', 'duration', 'weight_order', 'time_accept', 'time_done', 'tips',
                    'currency')
    list_display_links = (
        'price', 'destination_address', 'duration', 'weight_order', 'time_accept', 'time_done', 'tips',
        'currency')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fio', 'country', 'city')


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('fio', 'rate', 'phone_number')
