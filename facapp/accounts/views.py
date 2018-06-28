from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def SignUp(request):
    """ Nesta função da view é tratado sobre o cadastramento do usuário.
    Ela recebe o metodo POST, verifica se o formulário foi preenchido corretamente.
    Se sim, é feito o login automaticamente.
    Se não, mostra-se uma mensagem de erro conforme qual erro foi detectado e mostra novamente o formulário de registro .
    """
    data = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('url_index')
    else:
        form = SignUpForm()
    data['form'] = form
    return render(request, 'registration/signup.html', data)
