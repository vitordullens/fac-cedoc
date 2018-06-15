from django.shortcuts import render, redirect, HttpResponse
from .models import Doc, CampusJournal
from .forms import JournalUpload, AudioUpload, VideoUpload, SignUpForm
from facapp.settings import MEDIA_ROOT
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import os

# Create your views here.

def index(request):
    data = {}
    data['files'] = Doc.objects.all()
    return render(request, 'cedoc/index.html', data)

def SignUp(request):
    data = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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


def option(request):
    return render(request, 'cedoc/option.html')

def new_entry(request, btn):
    data = {}
    form = ""
    if(btn == 'journal'):
        form = JournalUpload(request.POST or None, request.FILES or None, initial={'description': "Coleção de jornal de laboratório editado pela Faculdade de Comunicação da UnB."})
        data['file'] = "JORNAL CAMPUS"
    elif(btn == 'video'):
        form = VideoUpload(request.POST or None, request.FILES or None)
        data['file'] = "VIDEO"
    else:
        form = AudioUpload(request.POST or None, request.FILES or None)
        data['file'] = "AUDIO"
    if form.is_valid():
        form.save()
        return redirect('url_index')
    data['form'] = form
    return render(request, 'cedoc/new_entry.html', data)

def delete(request, pk):
    doc = Doc.objects.get(pk=pk)
    if(doc.fileType == '.txt' or doc.fileType == '.md' or doc.fileType == '.pdf'):
        text = CampusJournal.objects.get(pk=pk).File
        os.remove(os.path.join(MEDIA_ROOT, str(text)))
    doc.delete()
    return redirect('url_index')