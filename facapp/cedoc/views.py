from django.shortcuts import render, redirect
from .models import Doc
from .forms import ImageUpload, TextUpload

# Create your views here.

def index(request):
    data = {}
    data['files'] = Doc.objects.all()
    return render(request, 'cedoc/index.html', data)

def option(request):
    return render(request, 'cedoc/option.html')

def new_image(request):
    data = {}
    form = ImageUpload(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_index')
    data['form'] = form
    return render(request, 'cedoc/new_image.html', data)

def new_text(request):
    data = {}
    form = TextUpload(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_index')
    data['form'] = form
    return render(request, 'cedoc/new_text.html', data)

