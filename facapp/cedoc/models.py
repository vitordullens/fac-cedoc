from django.db import models
from .validators import validate_AudioVisual, validate_CampusJournal, validate_CampusReporter
import datetime
import django

def getFileFormat():
    return (
        ('AN', 'Arquivo Físico'),
        ('UR', 'URL'),
        ('DG', 'Arquivo Digital')
    )

def coverage():
    return (
        ('L', 'Local'),
        ('R', 'Regional'),
        ('I', 'Internacional'),
        ('N', 'Nacional')
    )

def accept():
    return(
        (True, 'Sim'),
        (False, 'Nao'),
    )
    
class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=100)

    def __str__(self):
        return self.categoria

# Create your models here.
class Doc(models.Model):

    # TITLE START - includes many fields
    title = models.CharField('Título', max_length=300, default='Sem título', help_text="Nome do documento")
    description = models.TextField('Descrição', blank=True)
    publisher = models.CharField('Editor', max_length=150, default="FAC-UnB")
    # TODO: create options specific for each kind of document
    coverage = models.CharField('Cobertura', max_length=2, default='R', choices=coverage())
    rights = models.CharField('Direitos', max_length=100, default='Creative Commons', help_text="Direitos de acesso")
    source = models.CharField('Fonte', default='Faculdade de Comunicação - FAC' , max_length=100)
    date = models.DateField('Data do Documento', default=django.utils.timezone.now, help_text="Use formato dd/mm/AAAA")
    fileFormat = models.CharField('Formato de media', max_length=2, choices=getFileFormat(), default='DG', help_text='Escolha apenas 1 opção')
    language = models.CharField('Língua', max_length=50, default='Português')
    submissionDate = models.DateField(auto_now_add=True)
    accepted = models.BooleanField('Accept file', choices=accept(), default=False)
    sender = models.CharField(max_length=50, default="Anônimo")
    url = models.URLField('URL para Documento', blank=True)

    def __str__(self):
        return self.title

class CampusJournal(Doc):

    def __init__(self, *args, **kwargs):
        super(CampusJournal, self).__init__(*args, **kwargs)
        self.description = "Coleção de jornal de laboratório editado pela Faculdade de Comunicação da UnB."
    
    author = models.CharField('Autor', max_length=50, default='Jornalismo')
    produtor = models.CharField('Produtor', max_length=100, default="Faculdade de Comunicação da Universidade de Brasília")
    editor = models.CharField('Editor', max_length=100, default="Faculdade de Comunicação da Universidade de Brasília")
    collaborator = models.CharField('Colaborador', max_length=100, default="CEDOC")
    license = models.CharField('Licença', max_length=50, default='CC BY-NC-ND 4.0')
    repoLocation = models.CharField('Localização na Coleção', max_length=100, default='Coleções Especiais - BCE')
    cedocLocation = models.CharField('Localização no CEDOC', max_length=100, default='Arquivo Físico')
    size = models.CharField('Dimensões físicas', max_length=100, default='26.00 x 40.00 cm', help_text='Em centímetros')
    notas = models.TextField('Notas', blank=True)
    grafica = models.CharField('Gráfica', max_length=100, blank=True)
    File = models.FileField(upload_to='texts/jornal/', blank=True, validators=[validate_CampusJournal])

class CampusReporter(Doc):
    subject = models.CharField('Assunto', max_length=100, blank=True)
    collaborator = models.CharField('Colaborador', max_length=100, default="CEDOC")
    address = models.CharField('Endereço', max_length=150, default='CEDOC - FAC - UnB')
    printing = models.CharField('Impressão',  max_length=50, blank=True)
    tiragem = models.CharField('Tiragem', max_length=50, blank=True)
    File = models.FileField(upload_to='texts/reporter/', blank=True, validators=[validate_CampusReporter])

class AudioVisual(Doc):
    dateProduction = models.DateField('Data de produção', default=django.utils.timezone.now)
    material = models.CharField('Material Original', max_length=100, blank=True)
    country = models.CharField('País de Produção', max_length=50, default='Brasil')
    state = models.CharField('Estado de Produção', max_length=50, default='DF')
    city = models.CharField('Cidade de Produção', max_length=50, default='Brasília')
    string = str(country) + ',' + str(state) + ',' + str(city)
    locationProduction = models.CharField('Localização da Produção', max_length=200, default=string)
    duration = models.DurationField('Duração do Vídeo', default=datetime.timedelta(0), help_text="Use formato hh:mm:ss")
    categories = models.ManyToManyField(Categoria)
    File = models.FileField(upload_to='video/', blank=True, validators=[validate_AudioVisual])

class Contributor(models.Model):
    contributor = models.CharField('Contribuidor', max_length=100, help_text='Nome do contribuidor')
    role = models.CharField('Papel', max_length=100, help_text='Papel do contribuidor no projeto')
    paper = models.ForeignKey(Doc, on_delete=models.CASCADE)

    def __str__(self):
        name = self.contributor + "," + self.role + ". Participando em " + Doc.objects.filter(pk=self.paper)
        return name

class Certificate(models.Model):
    certificate = models.CharField('Certificado', max_length=100, help_text='Nome do certificado')
    date = models.DateField('Data do Certificado', default=django.utils.timezone.now, blank=True)
    paper = models.ForeignKey(AudioVisual, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificate

class Index(models.Model):
    materia = models.CharField('Matéria', max_length=100, help_text="Nome da Matéria")
    author = models.CharField('Autor', max_length=100, help_text="Nome do Autor")
    paper = models.ForeignKey(CampusJournal, on_delete=models.CASCADE)

    def __str__(self):
        return self.materia + ", por " + self.author