import os
from django.core.exceptions import ValidationError

def validate_CampusJournal(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Only PDF Files are accepted.')