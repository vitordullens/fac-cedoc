from django import forms
from django.forms import ModelForm, DateField, widgets, DateInput, Select
from .models import Doc, CampusJournal, AudioFile, VideoFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(DateInput):
    input_type = 'date'

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

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
