from django.contrib import admin
from .models import CampusJournal, CampusReporter, AudioVisual, Categoria

# Register your models here.
admin.site.register(CampusJournal)
admin.site.register(CampusReporter)
admin.site.register(AudioVisual)
admin.site.register(Categoria)
