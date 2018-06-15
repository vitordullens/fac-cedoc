from django.forms import ModelForm, DateField, widgets, DateInput, Select
from .models import Doc, CampusJournal, AudioFile, VideoFile, Contributor

class DateInput(DateInput):
    input_type = 'date'

class JournalUpload(ModelForm):

    class Meta:
        model = CampusJournal
        fields = ['title', 'description', 'publisher', 'coverage', 'rights', 'source', 'fileFormat', 'date', 'fileType', 'language', 'author', 'produtor', 'editor', 'collaborator', 'size', 'notas','grafica', 'File']
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

class ContribUpload(ModelForm):
    prefix = 'contributor'

    def setPrefix(self, str):
        self.prefix = str

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
            'role' : Select(choices=ROLES)
        }
