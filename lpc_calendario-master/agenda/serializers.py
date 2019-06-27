from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agenda.models import Agenda, Convite, Compromisso


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = True)
    class Meta:
        model = Agenda
        fields = ('nome', 'tipo','usuario')

class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    agenda = AgendaSerializer(many = False)
    class Meta:
        model = Compromisso
        fields = ('nome','dataHora','local', 'notas', 'agenda')

class ConviteSerializer(serializers.HyperlinkedModelSerializer):
    anfitriao = UserSerializer(many = False)
    compromisso = CompromissoSerializer(many = False)
    convidados = UserSerializer(many = True)
    class Meta:
        model = Convite
        fields = ('anfitriao','compromisso','convidados')
