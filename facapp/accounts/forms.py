from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    """ Este é o formulário de criação do usuário.
    Ele utiliza parte do formulário disponibilizado pelo próprio django - 'UserCreationForm' - e o modelo de usuário do mesmo - 'User'.
    Além do formulário padrão foi adicionado o campo email.
    Nele existe um texto de ajuda que é mostrado na tela, uma função extra de validação para emails da UnB 'RegexValidator' que possui uma mensagem de erro, caso for inserido errado.
    """
    email = forms.EmailField(max_length=254, help_text='Obrigatório. Informe um endereço de email válido. Apenas emails da UnB são aceitos', validators=[RegexValidator(regex=r'^[\w\d\.]*@(?:aluno\.)?unb\.br$', message='Só são permitidos emails da UnB.', code='invalid_email'),])
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')