import os
from django.core.exceptions import ValidationError

def validate_CampusJournal(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Apenas arquivos PDF são aceitos.')

def validate_CampusReporter(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Apenas arquivos PDF são aceitos.')

def validate_AudioVisual(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.mp3', '.mp4']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Apenas arquivos MP3 e MP4 são aceitos.')