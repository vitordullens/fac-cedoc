from django.db import models

################################# ACCEPTED FILE TYPES
def getFileFormats():
    return (
        ('.pdf', 'Portable Document Format (PDF)'),
        ('.txt', 'Documento de Texto'),
        ('.doc', 'Documento do Word'),
        ('.jpg', 'Imagem JPG'),
        ('.png', 'Portable Network Graphics (PNG)'),
        ('.mp3', 'Arquivo de Áudio MP3'),
    )

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    publisher = models.CharField(max_length=150)
    fileType = models.CharField(max_length=5, choices=getFileFormats(), default='txt')
    language = models.CharField(max_length=50)
    # relation (nao sei o que eh isso)
    coverage = models.CharField(max_length=50)
    rights = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    date = models.DateTimeField('Document Date')
    fileFormat = models.CharField(max_length=50)
    submissionDate = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Contributor(models.Model):
    contributor = models.CharField(max_length=100)
    paper = models.ForeignKey('Doc', on_delete=models.CASCADE)

class Image(Doc):
    Image = models.ImageField(upload_to='images/')

class TextFile(Doc):
    File = models.FileField(upload_to='texts/')
