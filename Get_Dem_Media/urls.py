from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
]

# To facilitate the uploads of media files to the website... To help create the media url for an image file.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
