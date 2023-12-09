from django.core.management import BaseCommand

from payments.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment_list = [
            {"user": 1, "date": "2023-12-09T15:13:51.972Z",
             "amount": "5070.0", "payment_method": "Card", "course_payment": 1},
            {"user": 1, "date": "2023-12-06T15:13:59.972Z",
             "amount": "7800.0", "payment_method": "Card", "lesson_payment": 2},
            {"user": 1, "date": "2023-12-07T15:13:51.972Z",
             "amount": "5000.0", "payment_method": "Card", "course_payment": 2},
            {"user": 1, "date": "2023-12-08T15:16:51.972Z",
             "amount": "18000.0", "payment_method": "Card", "lesson_payment": 1}
        ]

        payment_for_create = []

        for payment in payment_list:
            payment_for_create.append(
                Payment(**payment)
            )
        Payment.objects.bulk_create(payment_for_create)