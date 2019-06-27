from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *
from agenda.serializers import *



def todasAgendas(request):
    retorno = "<h1> TODAS AGENDAS CADASTRADAS </h1>"
    listaAgendas = Agenda.objects.all()
    for a in listaAgendas:
        retorno += '<br> Nome Agenda: {} <br> Agenda criada por: {} <br> Tipo Agenda: {} <br> <br> '.format(a.nome, a.usuario, a.tipo)
    return HttpResponse(retorno)

def get_userAgendas_byID(request, id):
    retorno = "<h1> AGENDAS PÚBLICAS DE FULANINHO </h1>"
    listaAgendasPublicas = Agenda.objects.filter(tipo='Publica',usuario__id=id)
    for a in listaAgendasPublicas:
        retorno += '<br> Nome Agenda: {} <br> <br> '.format(a.nome)
    return HttpResponse(retorno)

def agendaInstitucional(request):
    retorno = "<h1> TODOS OS COMPROMISSOS INSTITUCIONAIS </h1>"
    listaCompromissosInstitucionais = Compromisso.objects.filter(agenda__tipo='Institucional')
    for c in listaCompromissosInstitucionais:
        retorno += '<br> Nome Compromisso: {} <br> <br> '.format(c.nome)
    return HttpResponse(retorno)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class CompromissoViewSet(viewsets.ModelViewSet):
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    serializer_class = ConviteSerializer


# Create your views here.
#a = AgendaPublica.objects.get(pk=id)
