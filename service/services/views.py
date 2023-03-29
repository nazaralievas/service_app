from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Prefetch, F

from .models import Subscription, Client
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email'))
        ).annotate(price=F('service__full_price') -
                   F('service__full_price') * F('plan__discount_percent') / 100.00)
    serializer_class = SubscriptionSerializer
