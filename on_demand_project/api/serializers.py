from rest_framework.serializers import ModelSerializer
from .models import Courier, Currency, Client, Invoice


class CourierSerializer(ModelSerializer):
    class Meta:
        model = Courier
        fields = ('fio', 'rate', 'phone_number')


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ('name', )


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('fio', 'country', 'city')


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('price', 'destination_address', 'duration', 'weight_order', 'time_accept', 'time_done',
                  'tips', 'currency')
