from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

def validateEmail(email):
    if re.match(r'^[\w\d\.]*@(?:aluno\.)?unb\.br$', email):
        raise ValidationError(
            _('Only UnB email allowed'),
        )
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', validators=[RegexValidator(regex=r'^[\w\d\.]*@(?:aluno\.)?unb\.br$', message='Only UnB email allowed.', code='invalid_email'),])
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )