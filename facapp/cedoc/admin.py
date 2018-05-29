from django.contrib import admin
from .models import Image, TextFile, Contributor

# Register your models here.
admin.site.register(Image)
admin.site.register(TextFile)
admin.site.register(Contributor)