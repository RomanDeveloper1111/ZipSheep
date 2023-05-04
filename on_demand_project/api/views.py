from rest_framework.viewsets import ModelViewSet
from .models import Courier, Currency, Client, Invoice
from .serializers import CourierSerializer, ClientSerializer, CurrencySerializer, InvoiceSerializer
from rest_framework.permissions import IsAuthenticated


class CourierViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class CurrencyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ClientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class InvoiceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

