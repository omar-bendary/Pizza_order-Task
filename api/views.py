from .serializers import OrderSerializer
from .models import Order
from rest_framework import viewsets
from .permissions import IsEditableOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsEditableOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'customer_name']
