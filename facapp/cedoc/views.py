import os

from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from facapp.settings import MEDIA_ROOT

from .forms import AudioUpload, ContribUpload, JournalUpload, VideoUpload
from .models import AudioFile, CampusJournal, Contributor, Doc, VideoFile

# Functions
def getUnknownModel(request, pk):
    try:
        f = CampusJournal.objects.get(pk=pk)
        form = JournalUpload(request.POST or None, request.FILES or None, instance=f)
    except:
        try:
            f = AudioFile.objects.get(pk=pk)
            form = AudioUpload(request.POST or None, request.FILES or None, instance=f)
        except:
            try:
                f = VideoFile.objects.get(pk=pk)
                form = VideoUpload(request.POST or None, request.FILES or None, instance=f)
            except:
                pass # Talvez mudar para não deletar a entrada e retornar um erro ?
    return (f, form)
# Create your views here.

def index(request):
    data = {}
    files = {}
    if not request.user.is_superuser:
        docsOfUser = Doc.objects.filter(sender=request.user.username)
    else:
        docsOfUser = Doc.objects.all()
    for doc in docsOfUser:
        contribs = list(Contributor.objects.filter(paper=doc))
        files[doc] = contribs
    data['files'] = files
    return render(request, 'cedoc/index.html', data)

def edit(request, pk):
    (f, form) = getUnknownModel(request, pk)
    data = {}
    data['doc'] = f
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('url_index')
    return render(request, 'cedoc/edit.html', data)


def option(request):
    if request.user.is_authenticated:
        return render(request, 'cedoc/option.html')
    else:
        return HttpResponseForbidden()

def new_entry(request, btn):
    if request.user.is_authenticated:
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
            newEntry = form.save(commit=False)
            newEntry.sender = request.user.username
            newEntry.save()
            return redirect(reverse_lazy('url_contribs', args=[newEntry.pk]))
        data['form'] = form
        return render(request, 'cedoc/new_entry.html', data)
    else:
        return HttpResponseForbidden()

def delete(request, pk):
    if request.user.is_authenticated:
        doc = Doc.objects.get(pk=pk)
        (f, form) = getUnknownModel(request, pk)
        if f.File:
            os.remove(os.path.join(MEDIA_ROOT, str(f.File)))
        doc.delete()
        return redirect('url_index')
    else:
        return redirect('url_index')


def contribs(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = []
            i = int(request.POST['i'])
            for idx in range(i):
                string = 'contributor'+str(idx)
                forms.append( ContribUpload(request.POST or None, prefix=string))
                if not forms[idx].is_valid():
                    return HttpResponse("Deu ruim") # FIXME: one of the forms is not ok
            # if all forms are valid
            for form in forms:
                contrib = form.save(commit=False)
                contrib.paper = Doc.objects.get(pk=pk)
                contrib.save()
            return redirect('url_index')
        else:
            get = request.GET
            data = {}
            forms = []
            i = 0
            try:
                i = int(get['i']) + 1
            except:
                i = 1

            for idx in range(i):
                contrib = ContribUpload()
                contrib.setPrefix('contributor' + str(idx))
                idx += 1
                forms.append(contrib)
            data['doc'] = Doc.objects.get(pk=pk)
            data['forms'] = forms
            data['pk'] = pk 
            data['i'] = i
            return render(request, 'cedoc/contribs.html', data)
    else:
        return HttpResponseForbidden()
