from django.shortcuts import render

from .models import *


# Create your views here


# pages terminale bac melec

def accueil(request):
    return render(request, 'melec/accueil.html', {})


def realisation_Tale(request):
    evalRea = evaluation_Realisation.objects.filter(annee='Tale').order_by('candidat_id')
    return render(request, 'melec/realisation.html', {'evalRea': evalRea})


# essai

def filtre(request, pk):
    filtre_nom = attribution_d_un_chantier.objects.all().order_by('electricien')
    return render(request, 'melec/filtre.html', {'filtre_nom': filtre_nom})


# fin essai


def preparation_Tale(request):
    evalPrepa = evaluation_Preparation.objects.filter(annee='Tale').order_by('candidat_id')
    return render(request, 'melec/preparation.html', {'evalPrepa': evalPrepa})


def mise_en_service_Tale(request):
    evalMise = evaluation_Mise_en_service.objects.filter(annee='Tale').order_by('candidat_id')
    return render(request, 'melec/mise_en_service.html', {'evalMise': evalMise})


def maintenance_Tale(request):
    evalMaint = evaluation_Maintenance.objects.filter(annee='Tale').order_by('candidat_id')
    return render(request, 'melec/maintenance.html', {'evalMaint': evalMaint})


def communication_Tale(request):
    evalComm = evaluation_Communication.objects.filter(annee='Tale').order_by('candidat_id')
    return render(request, 'melec/communication.html', {'evalComm': evalComm})


# pages seconde bac melec

def realisation_2nde(request):
    evalRea = evaluation_Realisation.objects.filter(annee='2nde').order_by('candidat_id')
    return render(request, 'melec/realisation.html', {'evalRea': evalRea})


def preparation_2nde(request):
    evalPrepa = evaluation_Preparation.objects.filter(annee='2nde').order_by('candidat_id')
    return render(request, 'melec/preparation.html', {'evalPrepa': evalPrepa})


def mise_en_service_2nde(request):
    evalMise = evaluation_Mise_en_service.objects.filter(annee='2nde').order_by('candidat_id')
    return render(request, 'melec/mise_en_service.html', {'evalMise': evalMise})


def maintenance_2nde(request):
    evalMaint = evaluation_Maintenance.objects.filter(annee='2nde').order_by('candidat_id')
    return render(request, 'melec/maintenance.html', {'evalMaint': evalMaint})


def communication_2nde(request):
    evalComm = evaluation_Communication.objects.filter(annee='2nde').order_by('candidat_id')
    return render(request, 'melec/communication.html', {'evalComm': evalComm})


# pages premiere bac melec


def realisation_1ere(request):
    evalRea = evaluation_Realisation.objects.filter(annee='1ere').order_by('candidat_id')
    return render(request, 'melec/realisation.html', {'evalRea': evalRea})


def preparation_1ere(request):
    evalPrepa = evaluation_Preparation.objects.filter(annee='1ere').order_by('candidat_id')
    return render(request, 'melec/preparation.html', {'evalPrepa': evalPrepa})


def mise_en_service_1ere(request):
    evalMise = evaluation_Mise_en_service.objects.filter(annee='1ere').order_by('candidat_id')
    return render(request, 'melec/mise_en_service.html', {'evalMise': evalMise})


def maintenance_1ere(request):
    evalMaint = evaluation_Maintenance.objects.filter(annee='1ere').order_by('candidat_id')
    return render(request, 'melec/maintenance.html', {'evalMaint': evalMaint})


def communication_1ere(request):
    evalComm = evaluation_Communication.objects.filter(annee='1ere').order_by('candidat_id')
    return render(request, 'melec/communication.html', {'evalComm': evalComm})


# vue PDF

from django.http import HttpResponse
#from django_xhtml2pdf.utils import generate_pdf


def eleve(request):
    resp = HttpResponse(content_type='application/pdf')
    context = {
        'el': evaluation_Realisation.objects.filter(annee='Tale').order_by('candidat_id')
    }
 #   result = generate_pdf('el.html', file_object=resp, context=context)
   #return result
