from django.db import models
from django.utils import timezone


class Pytube(models.Model):
    switch = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    last_changed = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return 'Switch'

    class Meta:
        verbose_name_plural = "PyTube Switch"


class YoutubeDL(models.Model):
    switch = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    last_changed = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return 'Switch'

    class Meta:
        verbose_name_plural = "YouTube-DL Switch"
