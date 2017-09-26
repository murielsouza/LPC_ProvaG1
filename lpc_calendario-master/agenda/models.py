from django.db import models
from django.contrib.auth.models import User
from django import forms

class Agenda(models.Model):
    nome = models.CharField(max_length=128)
    usuario = models.ManyToManyField(User, blank=True, related_name='usuarios')

    TIPO_CHOICES = (
        ('Publica', 'Pública'),
        ('Privada', 'Privada'),
        ('Institucional','Institucional')
    )
    tipo = models.CharField(max_length=14, choices=TIPO_CHOICES, blank=False, null=False)

    #class Meta:
        #abstract = True

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    dataHora = models.DateTimeField(blank=True, null=True)
    local = models.CharField(max_length=60)
    notas = models.TextField()
    agenda = models.ForeignKey(Agenda, null=True, blank=False) #rever

    def __str__(self):
        return self.nome + "( " + self.agenda.nome + " )"


class Convite(models.Model):
    anfitriao = models.ForeignKey(User, null=True, blank=False)
    aceitar = models.BooleanField(default=False)
    convidados = models.ManyToManyField(User, blank=True, related_name='convidados')
    compromisso = models.ForeignKey(Compromisso, null=True, blank=False)

    def __str__(self):
        return self.anfitriao.username + " fez um convite para o evento " + self.compromisso.nome


# Create your models here.


'''class AgendaPublica(Agenda):
    categoria = 'Pública'

    def __str__(self):
        return self.categoria

class AgendaPrivada(Agenda):
    categoria = 'Privada'

    def __str__(self):
        return self.categoria

class AgendaInstitucional(Agenda):
    categoria = 'Institucional'

    def __str__(self):
        return self.categoria
'''
