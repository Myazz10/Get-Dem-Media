from django.contrib import admin
from .models import Audio, Video


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    search_fields = ['name', 'api', 'downloaded_on']
    list_filter = ['name', 'api', 'downloaded_on']
    list_display = ['name', 'api', 'downloaded_on']
    list_per_page = 30


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ['name', 'api', 'downloaded_on']
    list_filter = ['name', 'api', 'downloaded_on']
    list_display = ['name', 'api', 'downloaded_on']
    list_per_page = 30

