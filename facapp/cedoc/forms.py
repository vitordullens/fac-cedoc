from django.forms import ModelForm, DateField, widgets, DateInput
from .models import Doc, Contributor, Image

class DateInput(DateInput):
    input_type = 'date'

class UploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'subtitle', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'Image']
        widgets = {
            'date' : DateInput()
        }

