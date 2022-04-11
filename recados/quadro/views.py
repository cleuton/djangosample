from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Recado, Seguidor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def index(request):
	try:
		ultima_data = datetime.fromtimestamp(request.session['ultima_data'])
	except KeyError:
		ultima_data = datetime.now()
		request.session['ultima_data'] = datetime.timestamp(ultima_data)
	quantidade_recados = Recado.objects.count()
	template = loader.get_template('quadro/index.html')
	
	seus_recados = Recado.objects.filter(autor=request.user)
	recados_seguidos = []
	rs_seguindo = Seguidor.objects.filter(usuario_seguidor=request.user)
	for s in rs_seguindo:
		r_seguindo = Recado.objects.filter(autor=s.usuario_seguido)
		for r in r_seguindo:
			recados_seguidos.append(r)
	context = {
		'seus_recados' : seus_recados,
		'recados_seguidos' : recados_seguidos,
		'ultima_data' : ultima_data,
        'quantidade_recados': quantidade_recados,
    }
	nova_data = datetime.now()
	request.session['ultima_data'] = datetime.timestamp(nova_data)
	return HttpResponse(template.render(context, request))