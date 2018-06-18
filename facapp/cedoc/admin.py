from django.contrib import admin
from .models import CampusJournal, CampusReporter, AudioFile, VideoFile

# Register your models here.
admin.site.register(CampusJournal)
admin.site.register(CampusReporter)
admin.site.register(AudioFile)
admin.site.register(VideoFile)
# admin.site.register(Contributor)