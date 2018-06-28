from django.forms import ModelForm, DateField, widgets, DateInput, Select, ChoiceField, RadioSelect
from .models import Doc, CampusJournal, AudioVisual, Contributor, CampusReporter, Index, Certificate, Categoria

import django

class dateInput(DateInput):
    input_type = 'date'
    
class JournalUpload(ModelForm):

    class Meta:
        model = CampusJournal
        fields = ['title', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'language', 'author', 'produtor', 'editor', 'collaborator', 'size', 'notas','grafica', 'File', 'url']
        widgets = {
            'date' : dateInput()
        }

class ReporterUpload(ModelForm):

    class Meta:
        model = CampusReporter
        fields = ['title', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'language', 'subject', 'collaborator', 'address', 'printing', 'tiragem', 'File', 'url']
        widgets = {
            'date' : dateInput(),
        }
        
class AudioVisualUpload(ModelForm):
    class Meta:
        FORMATS = (
            ('.mp3', 'MP3 Audio'),
            ('.wav', 'Microsoft Wave (WAV)'),
            ('.aif', 'Audio Interchange File Format (AIFF)'),
        )

        model = AudioVisual
        fields = ['title', 'country', 'state', 'city', 'dateProduction','description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'duration', 'language', 'File', 'url']
        widgets = {
            'date' : dateInput(),
            'fileType' : Select(choices=FORMATS)
        }

class ContribUpload(ModelForm):
    prefix = 'contributor'

    def setPrefix(self, str):
        self.prefix += str

    class Meta:
        ROLES = (
            ('Ed_chefe', 'Editor(a) Chefe'),
            ('Ed_arte', 'Editor ou diretor de arte'),
            ('secr', 'Secretário(a)'),
            ('editor', 'Editor(a)'),
            ('secr_arte', 'Secretário de redação'),
            ('reporter', 'Repórter'),
            ('revisor', 'Revisor(a)'),
            ('ilust', 'Ilustrador(a)'),
            ('pj_graf', 'Projeto gráfico'),
            ('diagram', 'Diagramador'),
            ('prof', 'Professor'),
            ('fot', 'Fotógrafo'),
            ('jorn', 'Jornalista'),
            ('monit', 'Monitor(a)'),
            ('equipe', 'Equipe'),
            ('apoio', 'Apoio')
        )
        model = Contributor
        fields = ['contributor', 'role']
        widgets = {
            'role' : Select(choices=ROLES, attrs={'placeholder':"Selecione Papel"})
        }

class IndexUpload(ModelForm):
    prefix = 'index'

    def setPrefix(self, str):
        self.prefix += str

    class Meta:
        model = Index
        fields = ['materia', 'author']

class CertificateUpload(ModelForm):
    prefix = 'certificate'

    def setPrefix(self, str):
        self.prefix += str

    class Meta:
        model = Certificate
        fields = ['certificate', 'date']
        widgets = {
            'date': dateInput()
        }

class CategoryUpload(ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']


