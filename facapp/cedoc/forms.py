from django.forms import ModelForm
from .models import Doc, Contributor, Image

class UploadForm(ModelForm):
    class Meta:
        model = Doc
        fields = ['title', 'subtitle', 'description', 'publisher','language', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType']

