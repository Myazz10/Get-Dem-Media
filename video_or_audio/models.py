from django.db import models
from django.utils import timezone
# from cloudinary_storage.storage import VideoMediaCloudinaryStorage
# from cloudinary_storage.validators import validate_video


class Audio(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    api = models.CharField(max_length=50, null=True, blank=True)
    mp3 = models.FileField(upload_to='audios/', null=True, blank=True)#, storage=VideoMediaCloudinaryStorage(), validators=[validate_video])
    downloaded_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', '-downloaded_on']


class Video(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    api = models.CharField(max_length=50, null=True, blank=True)
    mp4 = models.FileField(upload_to='videos/', null=True, blank=True)#, storage=VideoMediaCloudinaryStorage(), validators=[validate_video])
    downloaded_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', '-downloaded_on']
