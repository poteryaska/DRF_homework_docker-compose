from celery import shared_task
from django.utils import timezone

from users.models import User
from celery.utils.log import logger


@shared_task
def block_inactive_users():
    logger.info("function started")
    # Определяем период неактивности (30 дней)
    inactive_period = timezone.now() - timezone.timedelta(days=30)

    # Ищем пользователей, не входивших в систему более месяца
    inactive_users = User.objects.filter(last_login__lt=inactive_period, is_active=True)
    inactive_users.update(is_active=False)
    inactive_users.save()
    logger.info("function ended")