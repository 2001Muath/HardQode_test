from django.db import models
from datetime import datetime


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=256)
    lesson_link = models.CharField(max_length=256)


class Product(models.Model):
    product_name = models.CharField(max_length=256)
    product_lessons = models.ManyToManyField(Lesson, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    price = models.PositiveIntegerField()
