from django.shortcuts import render, redirect, HttpResponse
from .models import Doc, CampusJournal, Contributor
from .forms import JournalUpload, AudioUpload, VideoUpload, ContribUpload
from django.urls import reverse_lazy
from facapp.settings import MEDIA_ROOT
import os

# Create your views here.

def index(request):
    data = {}
    data['files'] = Doc.objects.all()
    data['contribs'] = Contributor.objects.all()
    return render(request, 'cedoc/index.html', data)

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
        newEntry = form.save()
        return redirect(reverse_lazy('url_contribs', args=[newEntry.pk]))
    data['form'] = form
    return render(request, 'cedoc/new_entry.html', data)

def delete(request, pk):
    doc = Doc.objects.get(pk=pk)
    if(doc.fileType == '.txt' or doc.fileType == '.md' or doc.fileType == '.pdf'):
        text = CampusJournal.objects.get(pk=pk).File
        os.remove(os.path.join(MEDIA_ROOT, str(text)))
    doc.delete()
    return redirect('url_index')


def contribs(request, pk):

    if request.method == 'POST':
        forms = []
        i = int(request.POST['i'])
        for idx in range(i):
            string = 'contributor'+str(idx)
            forms.append( ContribUpload(request.POST or None, prefix=string))
            if not forms[idx].is_valid():
                return HttpResponse("Deu ruim") # one of the forms is not ok
        # if all forms are valid
        for form in forms:
            contrib = form.save(commit=False)
            contrib.paper = CampusJournal.objects.get(pk=pk)
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
        data['doc'] = CampusJournal.objects.get(pk=pk)
        data['forms'] = forms
        data['pk'] = pk 
        data['i'] = i
        return render(request, 'cedoc/contribs.html', data)

    