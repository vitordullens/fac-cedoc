from django.contrib import admin
from .models import Image, TextFile, AudioFile, VideoFile, Contributor

# Register your models here.
admin.site.register(Image)
admin.site.register(TextFile)
admin.site.register(AudioFile)
admin.site.register(VideoFile)
admin.site.register(Contributor)