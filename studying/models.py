from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    preview = models.ImageField(upload_to='static/course', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="lesson name")
    preview = models.ImageField(upload_to='static/lesson', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    url = models.URLField(verbose_name='url', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='name_course', null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'