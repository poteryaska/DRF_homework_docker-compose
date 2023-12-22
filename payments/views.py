from django.db.migrations import serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from payments.models import Payment
from payments.serializers import PaymentSerializer
import stripe


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def paument_create(self, serializer):
        payment = serializer.save()
        stripe.api_key = "pk_test_51OQ5WhB6xPKrOFgF4h2gDruKY4e99ratCgYbkh9IUc75yL4WrNzsVpEpbUHaTGJVnrzxegWwt4stS9Y9aAZzuBmE00WaW6nLh0"
        pay = stripe.PaymentIntent.create(
            amount=payment.amount,
            currency='usd',
            automatic_payment_methods={'enabled': True},)
        pay.save()
        return super().perform_create(serializer)


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_payment', 'lesson_payment', 'payment_method')
    ordering_fields = ('date',)

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()