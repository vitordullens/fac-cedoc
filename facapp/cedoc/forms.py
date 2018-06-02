from django.forms import ModelForm, DateField, widgets, DateInput, Select
from .models import Doc, Contributor, Image, TextFile, AudioFile, VideoFile

class DateInput(DateInput):
    input_type = 'date'

class ImageUpload(ModelForm):
    
    class Meta:
        FORMATS = (
        ('....', 'Photography Hard Copy'),
        ('.jpg', 'Imagem JPG'),
        ('.png', 'Portable Network Graphics (PNG)'),
        ('.gif', 'Graphics Interchange Format (GIF)'),
        ('.bmp', 'Windows bitmap (BMP)'),
        ('.cgm', 'Computer Graphics Metafile (CGM)'),
        ('.svg', 'Scalable Vector Graphics (SVG)'),
        ('.tif', 'Tagged Image File Format (TIFF)'),
        ('.cdr', 'CorelDRAW (CDR)'),
        ('.pdf', 'Portable Document Format (PDF)')
        )
        model = Image
        fields = ['title', 'subtitle', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'Image']
        widgets = {
            'date' : DateInput(),
            'fileType' : Select(choices=FORMATS)
        }

class TextUpload(ModelForm):

    class Meta:
        FORMATS = (
            ('book', 'Printed Book'),
            ('blet', 'Printed Booklet'),
            ('atrc', 'Printed Article'),
            ('.pdf', 'Portable Document Format (PDF)'),
            ('.txt', 'Text Document'),
            ('.doc', 'Microsoft Word Document'),
            ('.docx', 'Office Open XML (DOCX)'),
            ('.odt', 'OpenDocument TExt File (ODT)'),
            ('.epub', 'Eletronic Publication (EPUB)'),
            ('.html', 'HyperText Markup Language (HTML)'),
            ('.md',  'Markdown (MD)'),
            ('.csv', 'Comma Separated Values (CSV)'),
        )
        model = TextFile
        fields = ['title', 'subtitle', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'language', 'File']
        widgets = {
            'date' : DateInput(),
            'fileType' : Select(choices=FORMATS)
        }

class AudioUpload(ModelForm):
    class Meta:
        FORMATS = (
            ('.mp3', 'MP3 Audio'),
            ('.wav', 'Microsoft Wave (WAV)'),
            ('.aif', 'Audio Interchange File Format (AIFF)'),
        )

        model = AudioFile
        fields = ['title', 'subtitle', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'duration', 'fileType', 'language', 'File']
        widgets = {
            'date' : DateInput(),
            'fileType' : Select(choices=FORMATS)
        }

class VifdeoUpload(ModelForm):
    class Meta:
        FORMATS = (
            ('.mp4', 'MP4 Format'),
            ('.mpeg', 'MPEG Format'),
        )
        model = VideoFile
        fields = ['title', 'subtitle', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'duration', 'fileType', 'language', 'File']
        widgets = {
            'date' : DateInput(),
            'fileType' : Select(choices=FORMATS)
        }