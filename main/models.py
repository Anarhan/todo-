from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Books(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255, default=0)
    genre = models.CharField(max_length=255, default=0)
    year = models.CharField(max_length=255, default=0)
    date = models.DateTimeField(auto_now_add=True)
    is_favorites = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)

