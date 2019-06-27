"""calendario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from agenda.views import *
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'agendas', AgendaViewSet)
router.register(r'compromissos', CompromissoViewSet)
router.register(r'convites', ConviteViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^all/',todasAgendas, name='all'),
    url(r'^agenda/usuario/([0-9]{1})/',get_userAgendas_byID),
    url(r'^compromisso/', agendaInstitucional, name="Institucional"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
