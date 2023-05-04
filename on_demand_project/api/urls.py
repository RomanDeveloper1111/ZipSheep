from rest_framework import routers
from .views import CourierViewSet, ClientViewSet, CurrencyViewSet, InvoiceViewSet

urlpatterns = []
router = routers.SimpleRouter()
router.register(r'couriers', CourierViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'currencies', CurrencyViewSet)
router.register(r'invoices', InvoiceViewSet)
urlpatterns += router.urls
