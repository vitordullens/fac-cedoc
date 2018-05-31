from django.forms import ModelForm, DateField, widgets, DateInput
from .models import Doc, Contributor, Image, TextFile

class DateInput(DateInput):
    input_type = 'date'

class ImageUpload(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'subtitle', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'Image']
        widgets = {
            'date' : DateInput()
        }

class TextUpload(ModelForm):
    class Meta:
        model = TextFile
        fields = ['title', 'subtitle', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'language', 'File']
        widgets = {
            'date' : DateInput()
        }