from django.forms import ModelForm, DateField, widgets, DateInput, Select
from .models import Doc, Image, CampusJournal, AudioFile, VideoFile

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
        fields = ['title', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'Image']
        widgets = {
            'date' : DateInput(),
            'fileType' : Select(choices=FORMATS)
        }

class JournalUpload(ModelForm):

    class Meta:
        model = CampusJournal
        fields = ['title', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'language', 'author', 'produtor', 'editor', 'collaborator', 'size', 'File']
        widgets = {
            'date' : DateInput(),
        }

class AudioUpload(ModelForm):
    class Meta:
        FORMATS = (
            ('.mp3', 'MP3 Audio'),
            ('.wav', 'Microsoft Wave (WAV)'),
            ('.aif', 'Audio Interchange File Format (AIFF)'),
        )

        model = AudioFile
        fields = ['title', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'duration', 'fileType', 'language', 'File']
        widgets = {
            'date' : DateInput(),
            'fileType' : Select(choices=FORMATS)
        }

class VideoUpload(ModelForm):
    class Meta:
        FORMATS = (
            ('.mp4', 'MP4 Format'),
            ('.mpeg', 'MPEG Format'),
        )
        model = VideoFile
        fields = ['title', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'duration', 'fileType', 'language', 'File']
        widgets = {
            'date' : DateInput(),
            'fileType' : Select(choices=FORMATS)
        }