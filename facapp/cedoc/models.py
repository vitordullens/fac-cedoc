from django.db import models

################################# ACCEPTED FILE TYPES

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
# Create your models here.
class Doc(models.Model):
    title = models.CharField('Title', max_length=100)
    subtitle = models.CharField('Subtitle', max_length=150, blank=True)
    description = models.TextField('Description', blank=True)
    publisher = models.CharField('Publisher', max_length=150, default="FAC-UnB")
    fileType = models.CharField('File Format', max_length=5, default='.txt')
    coverage = models.CharField('Coverage', max_length=2, choices=coverage())
    rights = models.CharField('Rights', max_length=100)
    source = models.CharField('Source', max_length=100)
    date = models.DateField('Document Date')
    fileFormat = models.CharField('Media Format', max_length=2, choices=getFileFormat(), default='DG')
    submissionDate = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Contributor(models.Model):
    contributor = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Contributor")
    paper = models.ManyToManyField(Doc)
  
class Image(Doc):
    formats = (
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
    super.fileType.choices = formats
    Image = models.ImageField(upload_to='images/')

class TextFile(Doc):
    formats = (
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
    super.fileType.choices = formats
    language = models.CharField('Language', max_length=50, default='Português')
    File = models.FileField(upload_to='texts/')
