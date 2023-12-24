from django.conf import settings
from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='course name')
    preview = models.ImageField(upload_to='courses/', verbose_name='course preview', **NULLABLE)
    description = models.TextField(verbose_name='course description')
    course_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='owner course')
    price = models.CharField(default=100, **NULLABLE, verbose_name='price')
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='lesson name')
    description = models.TextField(verbose_name='lesson description')
    preview = models.ImageField(upload_to='lessons/', verbose_name='lesson preview', **NULLABLE)
    video = models.URLField(verbose_name='lesson video', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson', verbose_name='course')
    lesson_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner lesson')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

class Subscription(models.Model):
    """Класс для подписки"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscription', verbose_name='course')
    subscribed = models.BooleanField(default=False, verbose_name='status_subscribed')

    def __str__(self):
        return f"{self.user}: {self.course}"

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscribers'
