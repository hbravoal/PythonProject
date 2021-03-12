from django.http import HttpResponse
from django.template import Template, Context
import datetime


class Person():
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name

    

def saludo(request): #Primera vista
    return HttpResponse("Primear response")


def despedida(request): #Primera vista
    return HttpResponse("Despdida")

def dameFecha(request):
    fecha_actual = datetime.datetime.now
    return HttpResponse("fecha_actual")


def Home(request):
    person1= Person("Henry","Bravo")

    now= datetime.datetime.now
    singers= ['Bad Bonny','la rosalía','Daddy yankee']



    home_doc= open("E:/BIG/Projects/GitHub/PythonProject/Django/Proyecto1/Proyecto1/templates/index.html")
    plt=Template(home_doc.read())
    home_doc.close()

    ctx = Context({"person_name":person1.name,"person_last_name":person1.last_name,"singers":singers})

    document= plt.render(ctx)

    return HttpResponse(document)
