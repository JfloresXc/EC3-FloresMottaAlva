from multiprocessing import context
from django.shortcuts import HttpResponse
from django.template import Context, Template

# Create your views here.
def inicio(request):
    plantilla = open('C:/Users/JOSE/Documents/Universidad/SEXTO CICLO/LP3/2020-LP3-Python/semana-12/django/FloresMottaAlvaUC3/miapp/views/inicio.html')
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def uc3(request):
    plantilla = open('C:/Users/JOSE/Documents/Universidad/SEXTO CICLO/LP3/2020-LP3-Python/semana-12/django/FloresMottaAlvaUC3/miapp/views/uc3.html')
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def noticia(request):
    plantilla = open('C:/Users/JOSE/Documents/Universidad/SEXTO CICLO/LP3/2020-LP3-Python/semana-12/django/FloresMottaAlvaUC3/miapp/views/noticia.html')
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)