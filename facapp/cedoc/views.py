import os

from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from facapp.settings import MEDIA_ROOT

from .forms import ContribUpload, JournalUpload, ReporterUpload, AudioVisualUpload, IndexUpload, CertificateUpload, CategoryUpload
from .models import CampusJournal, CampusReporter, AudioVisual, Contributor, Doc, Categoria

# Functions
def getUnknownModel(request, pk):
    try:
        f = CampusJournal.objects.get(pk=pk)
        form = JournalUpload(request.POST or None, request.FILES or None, instance=f)
    except:
        try:
            f = AudioVisual.objects.get(pk=pk)
            form = AudioVisualUpload(request.POST or None, request.FILES or None, instance=f)
        except:
            try:
                f = CampusReporter.objects.get(pk=pk)
                form = ReporterUpload(request.POST or None, request.FILES or None, instance=f)
            except:
                f = None
                form = None
    return (f, form)
# Create your views here.

def index(request):
    data = {}
    files = {}
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            docsOfUser = Doc.objects.filter(sender=request.user.username)
        else:
            docsOfUser = Doc.objects.all()
        for doc in docsOfUser:
            contribs = list(Contributor.objects.filter(paper=doc))
            files[doc] = contribs
        data['files'] = files
        return render(request, 'cedoc/index.html', data)
    else:
        return redirect(reverse_lazy('login'))

def edit(request, pk):
    (f, form) = getUnknownModel(request, pk)
    data = {}
    data['doc'] = f
    data['form'] = form
    c  = Contributor.objects.filter(paper=pk)
    data['contributors'] = c
    if request.method == 'POST':
        if 'val' in request.POST:   # validate form
            print("Validando o form")
            if form.is_valid:
                entry = form.save(commit=False)
                entry.accepted = True
                entry.save()
                return redirect('url_index')
        else:   # delete contributor
            contribPk = request.POST['del']
            try:
                Contributor.objects.get(pk=contribPk).delete()
            except:
                pass    # contribuidor nao existe mais
            # reload page from beginning
            return redirect(reverse_lazy('url_edit', args=[pk]))
    return render(request, 'cedoc/edit.html', data)


def option(request):
    if request.user.is_authenticated:
        data = {}
        if request.user.is_superuser:
            form = CategoryUpload(request.POST or None)
            data['form'] = form
            data['string'] = ''
            if request.method == 'POST':
                if form.is_valid and request.user.is_superuser:
                    form.save()     # saves new category
                    data['string'] = 'Nova categoria salva!'
                    data['form'] = None
            return render(request, 'cedoc/option.html', data)
        return render(request, 'cedoc/option.html', data)
    else:
        return HttpResponseForbidden()

def new_entry(request, btn):
    if request.user.is_authenticated:
        data = {}
        form = ""
        if(btn == 'journal'):
            form = JournalUpload(request.POST or None, request.FILES or None, initial={'description': "Coleção de jornal de laboratório editado pela Faculdade de Comunicação da UnB."})
            data['file'] = "JORNAL CAMPUS"
        elif(btn == 'reporter'):
            form = ReporterUpload(request.POST or None, request.FILES or None)
            data['file'] = "CAMPUS REPORTER"
        else:
            form = AudioVisualUpload(request.POST or None, request.FILES or None)
            data['file'] = "AUDIOVISUAL"
            data['cat'] = Categoria.objects.all()

        if form.is_valid():
            newEntry = form.save(commit=False)
            newEntry.sender = request.user.username
            newEntry.save()
            if data['file'] == "AUDIOVISUAL":
                categories = request.POST.getlist('categorias')
                if len(categories) > 0:
                    for c in categories:
                        newEntry.categories.add(Categoria.objects.get(pk=c))
                return redirect(reverse_lazy('url_certificates', args=[newEntry.pk]))
            elif data['file'] == "JORNAL CAMPUS":
                return redirect(reverse_lazy('url_idx', args=[newEntry.pk]))
            else:
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

def unboundForms(type, request):
    get = request.GET
    i = 0
    try:
        i = int(get['i']) + 1
    except:
        i = 1
    forms = []
    for idx in range(i):
        if type == 'contributor':
            form = ContribUpload()
        elif type == 'index':
            form = IndexUpload()
        else:
            form = CertificateUpload()
        form.setPrefix(str(idx))
        idx += 1
        forms.append(form)
    return (forms, i)

# TODO: contribs, idx and certificates function do basicly the same thing.
# REfactoring code would be nice

def contribs(request, pk):
    returnUrl = 'url_contribs'
    item = 'contribuidores'
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = []
            i = int(request.POST['i'])
            for idx in range(i):
                string = 'contributor'+str(idx)
                forms.append( ContribUpload(request.POST or None, prefix=string))
                if not forms[idx].is_valid():
                    data = {}
                    data['doc'] = Doc.objects.get(pk=pk)
                    data['forms'] = forms
                    data['pk'] = pk 
                    data['i'] = i
                    data['return'] = returnUrl
                    data['item'] = item
                    return render(request, 'cedoc/foreign.html', data)
            # if all forms are valid
            for form in forms:
                contrib = form.save(commit=False)
                contrib.paper = Doc.objects.get(pk=pk)
                contrib.save()
            return redirect('url_index')
        else:
            data = {}
            data['forms'], data['i'] = unboundForms('contributor', request)
            data['pk'] = pk 
            data['return'] = returnUrl
            data['item'] = item
            return render(request, 'cedoc/foreign.html', data)
    else:
        return HttpResponseForbidden()

# Indexes are for Journals
def idx(request, pk):
    returnUrl = 'url_idx'
    item = 'índeces'
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = []
            i = int(request.POST['i'])
            for idx in range(i):
                string = 'index'+str(idx)
                forms.append( IndexUpload(request.POST or None, prefix=string))
                if not forms[idx].is_valid():
                    data = {}
                    data['doc'] = CampusJournal.objects.get(pk=pk)
                    data['forms'] = forms
                    data['pk'] = pk 
                    data['i'] = i
                    data['return'] = returnUrl
                    data['item'] = item
                    return render(request, 'cedoc/foreign.html', data)
            # if all forms are valid
            for form in forms:
                idx = form.save(commit=False)
                idx.paper = CampusJournal.objects.get(pk=pk)
                idx.save()
            return redirect(reverse_lazy('url_contribs', args=[pk]))
        else:
            data = {}
            data['forms'], data['i'] = unboundForms('index', request)
            data['pk'] = pk 
            data['return'] = returnUrl
            data['item'] = item
            return render(request, 'cedoc/foreign.html', data)
    else:
        return HttpResponseForbidden()
    
# Certificates are for AudioVisual
def certificates(request, pk):
    returnUrl = 'url_certificates'
    item = 'certificados'
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = []
            i = int(request.POST['i'])
            for idx in range(i):
                string = 'certificate'+str(idx)
                forms.append( CertificateUpload(request.POST or None, prefix=string))
                if not forms[idx].is_valid():
                    data = {}
                    data['doc'] = AudioVisual.objects.get(pk=pk)
                    data['forms'] = forms
                    data['pk'] = pk 
                    data['i'] = i
                    data['return'] = returnUrl
                    data['item'] = item
                    return render(request, 'cedoc/foreign.html', data)
            # if all forms are valid
            for form in forms:
                contrib = form.save(commit=False)
                contrib.paper = AudioVisual.objects.get(pk=pk)
                contrib.save()
            return redirect(reverse_lazy('url_contribs', args=[pk]))
        else:
            data = {}
            data['forms'], data['i'] = unboundForms('certificate', request)
            data['pk'] = pk 
            data['return'] = returnUrl
            data['item'] = item
            return render(request, 'cedoc/foreign.html', data)
    else:
        return HttpResponseForbidden()