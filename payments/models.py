from django.conf import settings
from django.db import models
from studying.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}

class Payment(models.Model):

    class PaymentMethod(models.TextChoices):
        CARD = 'Card'
        TRANSFER = 'Transfer'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    date = models.DateTimeField(auto_now_add=True, verbose_name='payments date')
    amount = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='payments amount')
    payment_method = models.CharField(choices=PaymentMethod.choices, default=PaymentMethod.CARD, verbose_name='payments method')
    course_payment = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments', verbose_name='course')
    lesson_payment = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payments', verbose_name='lesson')

    def __str__(self):
        return f"Payment from {self.user} for {self.course_payment if self.course_payment else self.lesson_payment}"

    class Meta:
        verbose_name = 'payments'
        verbose_name_plural = 'payments'
        ordering = ['-date']
