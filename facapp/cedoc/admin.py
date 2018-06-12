from django.contrib import admin
from .models import Image, CampusJournal, AudioFile, VideoFile

# Register your models here.
admin.site.register(Image)
admin.site.register(CampusJournal)
admin.site.register(AudioFile)
admin.site.register(VideoFile)
# admin.site.register(Contributor)