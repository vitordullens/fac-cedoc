from django.db import models
import datetime
################################# ACCEPTED FILE TYPES
def getFileTypes():
    return (
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
        ('....', 'Photography Hard Copy'),
        ('.jpg', 'Imagem JPG'),
        ('.png', 'Portable Network Graphics (PNG)'),
        ('.gif', 'Graphics Interchange Format (GIF)'),
        ('.bmp', 'Windows bitmap (BMP)'),
        ('.cgm', 'Computer Graphics Metafile (CGM)'),
        ('.svg', 'Scalable Vector Graphics (SVG)'),
        ('.tif', 'Tagged Image File Format (TIFF)'),
        ('.cdr', 'CorelDRAW (CDR)'),
        ('.pdf', 'Portable Document Format (PDF)'),
        ('.mp3', 'MP3 Audio'),
        ('.wav', 'Microsoft Wave (WAV)'),
        ('.aif', 'Audio Interchange File Format (AIFF)'),
        ('.mp4', 'MP4 Format'),
        ('.mpeg', 'MPEG Format'),
    )

def getFileFormat():
    return (
        ('AN', 'Analog'),
        ('DG', 'Digital')
    )

def coverage():
    return (
        ('L', 'Local'),
        ('R', 'Regional'),
        ('I', 'International'),
        ('N', 'National')
    )

def accept():
    return(
        (True, 'Sim'),
        (False, 'Nao'),
    )
# Create your models here.
class Doc(models.Model):
    title = models.CharField('Title', max_length=100)
    subtitle = models.CharField('Subtitle', max_length=150, blank=True)
    description = models.TextField('Description', blank=True)
    publisher = models.CharField('Publisher', max_length=150, default="FAC-UnB")
    fileType = models.CharField('File Format', max_length=5, default='.txt', choices=getFileTypes())
    coverage = models.CharField('Coverage', max_length=2, choices=coverage())
    rights = models.CharField('Rights', max_length=100)
    source = models.CharField('Source', max_length=100)
    date = models.DateField('Document Date')
    fileFormat = models.CharField('Media Format', max_length=2, choices=getFileFormat(), default='DG')
    submissionDate = models.DateField(auto_now_add=True)
    accepted = models.BooleanField('Accept file', choices=accept(), default=False)

    

    def __str__(self):
        return self.title

class Contributor(models.Model):
    contributor = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Contributor")
    paper = models.ManyToManyField(Doc)
  
class Image(Doc):
    Image = models.ImageField(upload_to='images/', blank=True)

class TextFile(Doc):
    language = models.CharField('Language', max_length=50, default='Português')
    File = models.FileField(upload_to='texts/', blank=True)

class AudioFile(Doc):
    duration = models.DurationField('Audio Duration', default=datetime.timedelta(0))
    language = models.CharField('Language', max_length=50, default='None', blank=True)
    File = models.FileField(upload_to='audio/', blank=True)

class VideoFile(Doc):
    duration = models.DurationField('Video Duration', default=datetime.timedelta(0))
    language = models.CharField('Language', max_length=50, default='None', blank=True)
    File = models.FileField(upload_to='video/', blank=True)