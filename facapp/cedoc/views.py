from django.shortcuts import render, redirect
from .models import Doc
from .forms import UploadForm

# Create your views here.

def index(request):
    data = {}
    data['files'] = Doc.objects.all()
    return render(request, 'cedoc/index.html', data)

def new(request):
    data = {}
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_index')
    data['form'] = form
    return render(request, 'cedoc/new.html', data)


