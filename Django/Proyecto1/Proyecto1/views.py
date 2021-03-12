from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader
from django.shortcuts import render


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
    # home_doc = loader.get_template("index.html")
    diccionary= {"person_name":person1.name,"person_last_name":person1.last_name,"singers":singers}    
    # document= home_doc.render(diccionary)

    return render(request,"index.html",diccionary)
