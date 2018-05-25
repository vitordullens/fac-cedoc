from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>What time is it? %s. </body></html>" % now
    return HttpResponse(html)

def index(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/index.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)