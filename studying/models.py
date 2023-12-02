from django.db import models

# Create your models here.
class Course(models.Model):

    name = models.CharField(max_length=50, verbose_name="name")
    preview = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    preview = models.ImageField(null=True, blank=True)
    description = models.TextField()
    link = models.TextField()

    def __str__(self):
        return f'{self.name}'