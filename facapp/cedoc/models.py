from django.db import models

################################# ACCEPTED FILE TYPES
def getFileTypes():
    return (
        ('.pdf', 'Portable Document Format (PDF)'),
        ('.txt', 'Documento de Texto'),
        ('.doc', 'Documento do Word'),
        ('.md',  'Markdown (MD)'),
        ('.jpg', 'Imagem JPG'),
        ('.png', 'Portable Network Graphics (PNG)'),
        ('.mp3', 'Arquivo de Áudio MP3'),
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
# Create your models here.
class Doc(models.Model):
    title = models.CharField('Title', max_length=100)
    subtitle = models.CharField('Subtitle', max_length=150, blank=True)
    description = models.TextField('Description', blank=True)
    publisher = models.CharField('Publisher', max_length=150, default="FAC-UnB")
    fileType = models.CharField('File Format', max_length=5, choices=getFileTypes(), default='.txt')
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
    Image = models.ImageField(upload_to='images/')

class TextFile(Doc):
    language = models.CharField('Language', max_length=50, default='Português')
    File = models.FileField(upload_to='texts/')
