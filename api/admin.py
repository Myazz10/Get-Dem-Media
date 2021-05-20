from django.contrib import admin
from .models import Pytube, YoutubeDL


MAX_OBJECTS = 1


@admin.register(Pytube)
class PytubeAdmin(admin.ModelAdmin):
    list_display = ['show', 'switch', 'created', 'last_changed']

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

    def show(self, obj):
        return "PyTube"

    show.short_description = "API"


@admin.register(YoutubeDL)
class YoutubeDLAdmin(admin.ModelAdmin):
    list_display = ['show', 'switch', 'created', 'last_changed']

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

    def show(self, obj):
        return "YoutubeDL"

    show.short_description = "API"
