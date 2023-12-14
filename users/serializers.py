from django.contrib.auth.models import User
from rest_framework import serializers

from payments.models import Payment


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('date', 'amount', 'payment_method')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    payment_history = PaymentHistorySerializer(many=True, read_only=True, source="payments")
    class Meta:
        model = User
        fields = ('email', 'payment_history')
