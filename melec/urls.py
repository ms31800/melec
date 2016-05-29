from django.conf.urls import url

from . import views

# vues Tale

urlpatterns = [url(r'^$', views.accueil, name='accueil'), url(r'^Tr$', views.realisation_Tale, name='realisation_Tale'),

               url(r'^Tp$', views.preparation_Tale, name='preparation_Tale'),
               url(r'^Tmi$', views.mise_en_service_Tale, name='mise_en_service_Tale'),

               url(r'^Tma$', views.maintenance_Tale, name='maintenance_Tale'),
               url(r'^Tc$', views.communication_Tale, name='communication_Tale'),

               url(r'^f/(?P<pk>[0-9]+)/$', views.filtre, name='filtre'),

               # vues 2nde

               url(r'^2r$', views.realisation_2nde, name='realisation_2nde'),
               url(r'^2p$', views.preparation_2nde, name='preparation_2nde'),

               url(r'^2mi$', views.mise_en_service_2nde, name='mise_en_service_2nde'),
               url(r'^2ma$', views.maintenance_2nde, name='maintenance_2nde'),

               url(r'^2c$', views.communication_2nde, name='communication_2nde'),

               # vues 1ere

               url(r'^1r$', views.realisation_1ere, name='realisation_1ere'),
               url(r'^1p$', views.preparation_1ere, name='preparation_1ere'),

               url(r'^1mi$', views.mise_en_service_1ere, name='mise_en_service_1ere'),
               url(r'^1ma$', views.maintenance_1ere, name='maintenance_1ere'),

               url(r'^1c$', views.communication_1ere, name='communication_1ere'),

               # vue pdf

               url(r'^z$', views.eleve, name='eleve'),

               ]
