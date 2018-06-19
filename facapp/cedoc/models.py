from django.db import models
from .validators import validate_AudioVisual, validate_CampusJournal, validate_CampusReporter
import datetime
import django
################################# ACCEPTED FILE TYPES
def getFileTypes():
    return (
        ('book', 'Printed Book'),
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

    # TITLE START - includes many fields
    title = models.CharField('Title', max_length=300, default='Untitled', help_text="Name of the Document")
    description = models.TextField('Description', blank=True)
    publisher = models.CharField('Publisher', max_length=150, default="FAC-UnB")
    # TODO: create options specific for each kind of document
    fileType = models.CharField('File Format', max_length=5, default='.txt', choices=getFileTypes())
    coverage = models.CharField('Coverage', max_length=2, default='R', choices=coverage())
    rights = models.CharField('Rights', max_length=100, default='Free Access', help_text="Access Rights")
    source = models.CharField('Source', default='Faculdade de Comunicação - FAC' , max_length=100)
    date = models.DateField('Document Date', default=django.utils.timezone.now)
    fileFormat = models.CharField('Media Format', max_length=2, choices=getFileFormat(), default='DG')
    language = models.CharField('Language', max_length=50, default='Português')
    submissionDate = models.DateField(auto_now_add=True)
    accepted = models.BooleanField('Accept file', choices=accept(), default=False)
    sender = models.CharField(max_length=50, default="Anonymous")
    url = models.URLField('URL para Documento', blank=True)

    def __str__(self):
        return self.title

class CampusJournal(Doc):

    def __init__(self, *args, **kwargs):
        super(CampusJournal, self).__init__(*args, **kwargs)
        self.description = "Coleção de jornal de laboratório editado pela Faculdade de Comunicação da UnB."
    
    author = models.CharField('Author', max_length=50, default='Jornalismo')
    produtor = models.CharField('Producer', max_length=100, default="Faculdade de Comunicação da Universidade de Brasília")
    editor = models.CharField('Editor', max_length=100, default="Faculdade de Comunicação da Universidade de Brasília")
    collaborator = models.CharField('Collaborator', max_length=100, default="CEDOC")
    license = models.CharField('License', max_length=50, default='CC BY-NC-ND 4.0')
    repoLocation = models.CharField('Location in Collection', max_length=100, default='Coleções Especiais - BCE')
    cedocLocation = models.CharField('Location in CEDOC', max_length=100, default='Arquivo Físico')
    size = models.CharField('Physical Dimensions', max_length=100, default='26.00 x 40.00 cm', help_text='In centimeters')
    notas = models.TextField('Notas', blank=True)
    grafica = models.CharField('Gráfica', max_length=100, blank=True)
    File = models.FileField(upload_to='texts/jornal/', blank=True, validators=[validate_CampusJournal])

class CampusReporter(Doc):
    subject = models.CharField('Assunto', max_length=100, blank=True)
    collaborator = models.CharField('Collaborator', max_length=100, default="CEDOC")
    address = models.CharField('Endereço', max_length=150, default='CEDOC - FAC - UnB')
    printing = models.CharField('Impressão',  max_length=50, blank=True)
    tiragem = models.CharField('Tiragem', max_length=50, blank=True)
    File = models.FileField(upload_to='texts/reporter/', blank=True, validators=[validate_CampusReporter])

class AudioVisual(Doc):
    dateProduction = models.DateField('Production Field', default=django.utils.timezone.now)
    country = models.CharField('Country of Production', max_length=50, default='Brasil')
    state = models.CharField('Country of Production', max_length=50, default='DF')
    city = models.CharField('Country of Production', max_length=50, default='Brasília')
    string = str(country) + ',' + str(state) + ',' + str(city)
    locationProduction = models.CharField('Location of Production', max_length=200, default=string)
    duration = models.DurationField('Video Duration', default=datetime.timedelta(0))
    File = models.FileField(upload_to='video/', blank=True, validators=[validate_AudioVisual])

class Contributor(models.Model):
    contributor = models.CharField('Contributor', max_length=100, default='Unknown', help_text='Name of Contributor')
    role = models.CharField('Role', max_length=100, default="Contributor", help_text='Role of Contributor in the Project')
    paper = models.ForeignKey(Doc, on_delete=models.CASCADE)

    def __str__(self):
        name = self.contributor + "," + self.role + ". Participating in " + Doc.objects.filter(pk=self.paper)
        return name
