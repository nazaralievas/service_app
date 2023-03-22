from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField

from .models import Subscription


class SubscriptionSerializer(ModelSerializer):
    client_name = CharField(source='client.company_name')
    email = CharField(source='client.user.email')

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email')
