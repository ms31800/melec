from django.contrib import admin

from models import *


class eleveAdmin(admin.ModelAdmin):
    model = eleve
    list_display = ('nom', 'prenom', 'date_de_naissance')
    search_fields = ('nom', 'prenom')


class attribution_d_un_chantierAdmin(admin.ModelAdmin):
    model = attribution_d_un_chantier
    list_display = ('date', 'date_fin', 'Nb_heure', 'electricien', 'travail_eleve')
    search_fields = ('date', 'Nb_heure')


class evaluation_PreparationAdmin(admin.ModelAdmin):
    model = evaluation_Realisation
    list_filter = (
        'annee', 'nom', 'candidat', 'chantier_a_evaluer', 'statut', 'tache_Preparation', 'competenceC1', 'competenceC2',
        'competenceC3',
        'competenceC10', 'competenceC11', 'competenceC12', 'attitude_Preparation', 'appreciation', 'Note')


class evaluation_RealisationAdmin(admin.ModelAdmin):
    model = evaluation_Realisation
    list_filter = (
        'id', 'annee', 'candidat', 'nom', 'chantier_a_evaluer', 'statut', 'tache_Realisation', 'competenceC2',
        'competenceC4', 'competenceC5',
        'competenceC10', 'competenceC11', 'competenceC12', 'attitude_Realisation', 'appreciation', 'Note')


class evaluation_Mise_en_serviceAdmin(admin.ModelAdmin):
    model = evaluation_Mise_en_service
    list_filter = (
        'annee', 'nom', 'candidat', 'chantier_a_evaluer', 'statut', 'tache_Mise_en_service', 'competenceC2',
        'competenceC5',
        'competenceC6',
        'competenceC7', 'competenceC8', 'competenceC9', 'competenceC10', 'attitude_Mise_en_service', 'appreciation',
        'Note')


class evaluation_MaintenanceAdmin(admin.ModelAdmin):
    model = evaluation_Maintenance
    list_filter = (
        'annee', 'nom', 'candidat', 'chantier_a_evaluer', 'statut', 'tache_Maintenance', 'competenceC2', 'competenceC5',
        'competenceC6',
        'competenceC7', 'competenceC8', 'competenceC9', 'competenceC10', 'attitude_Maintenance', 'appreciation', 'Note')


class evaluation_CommunicationAdmin(admin.ModelAdmin):
    model = evaluation_Communication
    list_filter = (
        'annee', 'nom', 'candidat', 'chantier_a_evaluer', 'statut', 'tache_Communication', 'competenceC1',
        'competenceC10',
        'competenceC11',
        'competenceC12', 'competenceC13', 'attitude_Communication', 'appreciation', 'Note')


# Register your models here.
# admin.site.register(eleve)
admin.site.register(enseignant)
admin.site.register(eleve, eleveAdmin)
admin.site.register(chantier)
admin.site.register(tacheP)
admin.site.register(tacheR)
admin.site.register(tacheMi)
admin.site.register(tacheMa)
admin.site.register(tacheC)
# admin.site.register(competence)
admin.site.register(competenceC1)
admin.site.register(competenceC2)
admin.site.register(competenceC3)
admin.site.register(competenceC4)
admin.site.register(competenceC5)
admin.site.register(competenceC6)
admin.site.register(competenceC7)
admin.site.register(competenceC8)
admin.site.register(competenceC9)
admin.site.register(competenceC10)
admin.site.register(competenceC11)
admin.site.register(competenceC12)
admin.site.register(competenceC13)
admin.site.register(attitude)
admin.site.register(attribution_d_un_chantier, attribution_d_un_chantierAdmin)
admin.site.register(evaluation_Preparation, evaluation_PreparationAdmin)
admin.site.register(evaluation_Realisation, evaluation_RealisationAdmin)
admin.site.register(evaluation_Mise_en_service, evaluation_Mise_en_serviceAdmin)
admin.site.register(evaluation_Maintenance, evaluation_MaintenanceAdmin)
admin.site.register(evaluation_Communication, evaluation_CommunicationAdmin)
