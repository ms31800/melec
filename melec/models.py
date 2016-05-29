#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.

# enseignants des 3 niveau

class enseignant(models.Model):
    enseignant_nom = (
        ('M. Chaneau P', 'M. Chaneau P'),
        ('M. Chanfreau JF', 'M. Chanfreau JF'),
        ('M. Ducuing D', 'M. Ducuing D'),
        ('M. Sanchez M', 'M. Sanchez M'),
    )

    nom = models.CharField(max_length=20, choices=enseignant_nom, default='M. Chaneau P')

    def __unicode__(self):
        return u"{0} ".format(self.nom)


# eleves des 3 niveaux

class eleve(models.Model):
    nom = models.CharField(max_length=30, verbose_name="Nom")
    prenom = models.CharField(max_length=30, verbose_name="Prénom")
    date_de_naissance = models.DateField(verbose_name="Date de naissance")

    def __unicode__(self):
        return u"{0} {1} ({2})".format(self.nom, self.prenom, self.date_de_naissance)


class chantier(models.Model):
    chantier_type = (
        ('Domestique', 'Domestique'),
        ('Industriel', 'Industriel'),
        ('Tertiaire', 'Tertiaire'),
    )

    chantier_alim = (
        ('Mono', 'Mono'),
        ('Tri', 'Tri'),
        ('Courant faible', 'Courant faible'),
    )

    chantier_slt = (
        ('TT', 'TT'),
        ('TN', 'TN'),
        ('IT', 'IT'),
        ('sans objet', 'sans objet'),
        ('je ne sais pas', 'je ne sais pas'),
    )

    activite = models.CharField(max_length=130, verbose_name="Activité prévue")
    type = models.CharField(max_length=20, choices=chantier_type, default='Domestique')
    reseau = models.CharField(max_length=20, choices=chantier_alim, default='mono')
    slt = models.CharField(max_length=20, choices=chantier_slt, default='je ne sais pas')

    def __unicode__(self):
        return u"{0} (Type:{1}) (Reseau:{2}) (SLT:{3})".format(self.activite, self.type, self.reseau, self.slt)


# taches preparation

class tacheP(models.Model):
    tacheP_eval = (
        ('Conforme aux resultats attendus', 'Conforme aux resultats attendus'),
        ('NON conforme aux resultats attendus', 'Non conforme aux resultats attendus '),
        ('En phase d apprentissage', 'En phase d apprentissage'),
    )

    tache_1_1 = models.CharField(max_length=100, choices=tacheP_eval, default='En phase d apprentissage',
                                 verbose_name="T 1-1:prendre connaissance du dossier relatif aux opérations à réaliser, le constituer pour une opération simple")
    tache_1_2 = models.CharField(max_length=100, choices=tacheP_eval, default='En phase d apprentissage',
                                 verbose_name="T 1-2:rechercher et expliquer les informations relatives aux opérations et aux conditions d’exécution")
    tache_1_3 = models.CharField(max_length=100, choices=tacheP_eval, default='En phase d apprentissage',
                                 verbose_name="T 1-3:vérifier et compléter si nécessaire la liste des matériels, équipements et outillages nécessaires aux opérations")
    tache_1_4 = models.CharField(max_length=100, choices=tacheP_eval, default='En phase d apprentissage',
                                 verbose_name="T 1-4:répartir les tâches en fonction des habilitations, des certifications des équipiers et du planning des autres intervenants")

    def __unicode__(self):
        return u"T1-1:{0} - T1-2:{1} - T1-3:{2} - T1-4:{3} ".format(self.tache_1_1, self.tache_1_2, self.tache_1_3,
                                                                    self.tache_1_4)


# taches realisation referentiel

class tacheR(models.Model):
    tacheR_eval = (
        ('Conforme aux resultats attendus', 'Conforme aux resultats attendus'),
        ('NON conforme aux resultats attendus', 'Non conforme aux resultats attendus '),
        ('En phase d apprentissage', 'En phase d apprentissage'),
    )

    tache_2_1 = models.CharField(max_length=100, choices=tacheR_eval, default='En phase d apprentissage',
                                 verbose_name="T 2-1:organiser le poste de travail")
    tache_2_2 = models.CharField(max_length=100, choices=tacheR_eval, default='En phase d apprentissage',
                                 verbose_name="T 2-2:implanter, poser, installer les matériels électriques")
    tache_2_3 = models.CharField(max_length=100, choices=tacheR_eval, default='En phase d apprentissage',
                                 verbose_name="T 2-3:câbler, raccorder les matériels électriques")
    tache_2_4 = models.CharField(max_length=100, choices=tacheR_eval, default='En phase d apprentissage',
                                 verbose_name="T 2-4:gérer les activités de son équipe")
    tache_2_5 = models.CharField(max_length=100, choices=tacheR_eval, default='En phase d apprentissage',
                                 verbose_name="T 2-5:coordonner son activité par rapport à celles des autres intervenants")
    tache_2_6 = models.CharField(max_length=100, choices=tacheR_eval, default='En phase d apprentissage',
                                 verbose_name="T 2-6:mener son activité de manière éco-responsable")

    def __unicode__(self):
        return u"T2-1:{0} - T2-2:{1} - T2-3:{2} - T2-4:{3} - T2-5:{4} - T2-6:{5}".format(self.tache_2_1,
                                                                                         self.tache_2_2, self.tache_2_3,
                                                                                         self.tache_2_4, self.tache_2_5,
                                                                                         self.tache_2_6, )

        # taches mise en service


class tacheMi(models.Model):
    tacheMi_eval = (
        ('Conforme aux resultats attendus', 'Conforme aux resultats attendus'),
        ('NON conforme aux resultats attendus', 'Non conforme aux resultats attendus '),
        ('En phase d apprentissage', 'En phase d apprentissage'),
    )

    tache_3_1 = models.CharField(max_length=100, choices=tacheMi_eval, default='En phase d apprentissage',
                                 verbose_name="T 3-1:réaliser les vérifications, les réglages, les paramétrages, les essais nécessaires à la mise en service de l’installation")
    tache_3_2 = models.CharField(max_length=100, choices=tacheMi_eval, default='En phase d apprentissage',
                                 verbose_name="T 3-2:participer à la réception technique et aux levées de réserves de l’installation")

    def __unicode__(self):
        return u"T3-1:{0} - T3-2:{1}  ".format(self.tache_3_1, self.tache_3_2)


# taches maintenance

class tacheMa(models.Model):
    tacheMa_eval = (
        ('Conforme aux resultats attendus', 'Conforme aux resultats attendus'),
        ('NON conforme aux resultats attendus', 'Non conforme aux resultats attendus '),
        ('En phase d apprentissage', 'En phase d apprentissage'),
    )

    tache_4_1 = models.CharField(max_length=100, choices=tacheMa_eval, default='En phase d apprentissage',
                                 verbose_name="T 4-1:réaliser une opération de maintenance préventive")
    tache_4_2 = models.CharField(max_length=100, choices=tacheMa_eval, default='En phase d apprentissage',
                                 verbose_name="T 4-2:réaliser une opération de dépannage")

    def __unicode__(self):
        return u"T4-1:{0} - T4-2:{1}  ".format(self.tache_4_1, self.tache_4_2)


# taches communication

class tacheC(models.Model):
    tacheC_eval = (
        ('Conforme aux resultats attendus', 'Conforme aux resultats attendus'),
        ('NON conforme aux resultats attendus', 'Non conforme aux resultats attendus '),
        ('En phase d apprentissage', 'En phase d apprentissage'),
    )

    tache_5_1 = models.CharField(max_length=100, choices=tacheC_eval, default='En phase d apprentissage',
                                 verbose_name="T 5-1:participer à la mise à jour du dossier technique de l’installation")
    tache_5_2 = models.CharField(max_length=100, choices=tacheC_eval, default='En phase d apprentissage',
                                 verbose_name="T 5-2:échanger sur le déroulement des opérations, expliquer le fonctionnement de l’installation à l’interne et à l’externe")
    tache_5_3 = models.CharField(max_length=100, choices=tacheC_eval, default='En phase d apprentissage',
                                 verbose_name="T 5-3:conseiller le client, lui proposer une prestation complémentaire, une modification ou une amélioration")

    def __unicode__(self):
        return u"T5-1:{0} - T5-2:{1} - T5-3:{2} ".format(self.tache_5_1, self.tache_5_2, self.tache_5_3)


# competences referentiel

class competenceC1(models.Model):
    competenceC1_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C1 = models.SmallIntegerField(choices=competenceC1_choix,
                                  default='Non evaluee',
                                  verbose_name="C1:Analyser les conditions de l’opération et son contexte")

    def __unicode__(self):
        return u"C1:{0} ".format(self.C1)


class competenceC2(models.Model):
    competenceC2_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C2 = models.SmallIntegerField(choices=competenceC2_choix,
                                  default='Non evaluee', verbose_name="C2:Organiser l’opération dans son contexte")

    def __unicode__(self):
        return u"C2:{0} ".format(self.C2)


class competenceC3(models.Model):
    competenceC3_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C3 = models.SmallIntegerField(choices=competenceC3_choix,
                                  default=0,
                                  verbose_name="C3:Définir une installation à l’aide de solutions préétablies")

    def __unicode__(self):
        return u"C3:{0} ".format(self.C3)


class competenceC4(models.Model):
    competenceC4_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C4 = models.SmallIntegerField(choices=competenceC4_choix,
                                  default='Non evaluee',
                                  verbose_name="C4:Réaliser une installation de manière éco-responsable")

    def __unicode__(self):
        return u"C4:{0} ".format(self.C4)


class competenceC5(models.Model):
    competenceC5_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C5 = models.SmallIntegerField(choices=competenceC5_choix,
                                  default='Non evaluee',
                                  verbose_name="C5:Contrôler les grandeurs caractéristiques de l’installation")

    def __unicode__(self):
        return u"C5:{0} ".format(self.C5)


class competenceC6(models.Model):
    competenceC6_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C6 = models.SmallIntegerField(choices=competenceC6_choix,
                                  default='Non evaluee',
                                  verbose_name="C6:Régler, paramétrer les matériels de l’installation")

    def __unicode__(self):
        return u"C6:{0} ".format(self.C6)


class competenceC7(models.Model):
    competenceC7_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C7 = models.SmallIntegerField(choices=competenceC7_choix,
                                  default='Non evaluee', verbose_name="C7:Valider le fonctionnement de l’installation")

    def __unicode__(self):
        return u"C7:{0} ".format(self.C7)


class competenceC8(models.Model):
    competenceC8_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C8 = models.SmallIntegerField(choices=competenceC8_choix,
                                  default='Non evaluee', verbose_name="C8:Diagnostiquer un dysfonctionnement")

    def __unicode__(self):
        return u"C8:{0} ".format(self.C8)


class competenceC9(models.Model):
    competenceC9_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C9 = models.SmallIntegerField(choices=competenceC9_choix,
                                  default='Non evaluee', verbose_name="C9:Remplacer un matériel électrique")

    def __unicode__(self):
        return u"C9:{0} ".format(self.C9)


class competenceC10(models.Model):
    competenceC10_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C10 = models.SmallIntegerField(choices=competenceC10_choix,
                                   default='Non evaluee',
                                   verbose_name="C10:Exploiter les outils numériques dans le contexte professionnel")

    def __unicode__(self):
        return u"C10:{0} ".format(self.C10)


class competenceC11(models.Model):
    competenceC11_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C11 = models.SmallIntegerField(choices=competenceC11_choix,
                                   default='Non evaluee',
                                   verbose_name="C11:Compléter les documents liés aux opérations")

    def __unicode__(self):
        return u"C11:{0} ".format(self.C11)


class competenceC12(models.Model):
    competenceC12_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C12 = models.SmallIntegerField(choices=competenceC12_choix,
                                   default='Non evaluee',
                                   verbose_name="C12:Communiquer entre professionnels sur l’opération")

    def __unicode__(self):
        return u"C12:{0} ".format(self.C12)


class competenceC13(models.Model):
    competenceC13_choix = (
        (0, 'Non acquise'),
        (1, 'Acquise'),
        (2, 'Non evaluee'),
    )

    C13 = models.SmallIntegerField(choices=competenceC13_choix,
                                   default='Non evaluee',
                                   verbose_name="C13:Communiquer avec le client/usager sur l’opération")

    def __unicode__(self):
        return u"C13:{0} ".format(self.C13)


# attitude professionnelle

class attitude(models.Model):
    attitude_choix = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
        ('En progres', 'En progres'),
    )

    AP1 = models.CharField(max_length=100, choices=attitude_choix, default='Non evaluee',
                           verbose_name="AP1:faire preuve de rigueur et de précision")
    AP2 = models.CharField(max_length=100, choices=attitude_choix, default='Non evaluee',
                           verbose_name="AP2:faire preuve d’esprit d’équipe")
    AP3 = models.CharField(max_length=100, choices=attitude_choix, default='Non evaluee',
                           verbose_name="AP3:faire preuve de curiosité et d’écoute")
    AP4 = models.CharField(max_length=100, choices=attitude_choix, default='Non evaluee',
                           verbose_name="AP4:faire preuve d’initiative")
    AP5 = models.CharField(max_length=100, choices=attitude_choix, default='Non evaluee',
                           verbose_name="AP5:faire preuve d’analyse critique")

    def __unicode__(self):
        return u"AP1:{0} - AP2:{1} - AP3:{2} - AP4:{3} - AP5:{4}".format(self.AP1, self.AP2, self.AP3, self.AP4,
                                                                         self.AP5)


# Attribution chantier

class attribution_d_un_chantier(models.Model):
    attribution_d_un_chantier_statut = (
        ('Chantier termine', 'Chantier termine'),
        ('Termine hors delai', 'Termine hors delai'),
        ('Stoppe', 'Stoppe'),
        ('Absent', 'Absent'),
    )

    #    nom = models.ForeignKey(enseignant, on_delete=models.CASCADE, verbose_name="Enseignant responsable")
    date = models.DateField(verbose_name="Date de début de chantier")
    date_fin = models.DateField(verbose_name="Date de fin de chantier")
    Nb_heure = models.PositiveSmallIntegerField(verbose_name="Nombre d'heures prévues")
    electricien = models.ForeignKey(eleve, on_delete=models.CASCADE, verbose_name="électricien désigné")
    travail_eleve = models.ForeignKey(chantier, on_delete=models.CASCADE,
                                      verbose_name="Chantier affecté à un électricien")

    def __unicode__(self):
        return u"{0}  {1} - Durée du chantier:{2}h - {3} ".format(self.electricien.nom, self.electricien.prenom,
                                                                  self.Nb_heure, self.travail_eleve,
                                                                  )


# Evaluation REALISATION

class evaluation_Realisation(models.Model):
    evaluation_Realisation_statut = (
        ('Chantier termine', 'Chantier termine'),
        ('Termine hors delai', 'Termine hors delai'),
        ('Stoppe', 'Stoppe'),
        ('Absent', 'Absent'),
    )
    evaluation_Realisation_classe = (
        ('2nde', '2nde'),
        ('1ere', '1ere'),
        ('Tale', 'Tale'),
    )

    annee = models.CharField(max_length=7, choices=evaluation_Realisation_classe, default='2nde', verbose_name="Classe")
    nom = models.ForeignKey(enseignant, on_delete=models.CASCADE, verbose_name="Enseignant responsable")
    candidat = models.ForeignKey(eleve, on_delete=models.CASCADE, verbose_name="candidat")
    chantier_a_evaluer = models.ForeignKey(attribution_d_un_chantier, on_delete=models.CASCADE,
                                           verbose_name="chantier à évaluer")
    heurePass = models.PositiveSmallIntegerField(verbose_name="Nombre d'heures passées")
    statut = models.CharField(max_length=20, choices=evaluation_Realisation_statut, default='Absent')
    tache_Realisation = models.ForeignKey(tacheR, on_delete=models.CASCADE, verbose_name="Tâche(s) validée(s)")
    competenceC2 = models.ForeignKey(competenceC2, on_delete=models.CASCADE, verbose_name="C2")
    competenceC4 = models.ForeignKey(competenceC4, on_delete=models.CASCADE, verbose_name="C4")
    competenceC5 = models.ForeignKey(competenceC5, on_delete=models.CASCADE, verbose_name="C5")
    competenceC10 = models.ForeignKey(competenceC10, on_delete=models.CASCADE, verbose_name="C10")
    competenceC11 = models.ForeignKey(competenceC11, on_delete=models.CASCADE, verbose_name="C11")
    competenceC12 = models.ForeignKey(competenceC12, on_delete=models.CASCADE, verbose_name="C12")
    attitude_Realisation = models.ForeignKey(attitude, on_delete=models.CASCADE,
                                             verbose_name="attitude(s) professionnelle(s) acquise(s)")
    appreciation = models.CharField(max_length=150, verbose_name="Appréciation")
    Note = models.PositiveSmallIntegerField(verbose_name="Note proposée /20")

    def __unicode__(self):
        return u"{0} {1}: {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9} - {10} - {11} - {12} - {13} - {14}  {15} - {16} - {17} - {18} - {19} - {20} - {21} - {22} - {23} - {24} - {25} {26} ".format(
            self.annee,
            self.chantier_a_evaluer.electricien, self.chantier_a_evaluer.date, self.chantier_a_evaluer.travail_eleve,
            self.chantier_a_evaluer.Nb_heure,
            self.tache_Realisation.tache_2_1, self.tache_Realisation.tache_2_2, self.tache_Realisation.tache_2_3,
            self.tache_Realisation.tache_2_4,
            self.tache_Realisation.tache_2_5, self.tache_Realisation.tache_2_6, self.competenceC2.C2,
            self.competenceC4.C4, self.competenceC5.C5,
            self.competenceC10.C10, self.competenceC11.C11, self.competenceC12.C12, self.attitude_Realisation.AP1,
            self.attitude_Realisation.AP2,
            self.attitude_Realisation.AP3, self.attitude_Realisation.AP4, self.attitude_Realisation.AP5, self.statut,
            self.appreciation,
            self.Note, self.heurePass, self.id)


# evaluation PREPARATION

class evaluation_Preparation(models.Model):
    evaluation_Preparation_statut = (
        ('Preparation chantier terminee', 'Preparation chantier terminee'),
        ('Terminee hors delai', 'Terminee hors delai'),
        ('Stoppe', 'Stoppe'),
        ('Absent', 'Absent'),
    )
    evaluation_Preparation_classe = (
        ('2nde', '2nde'),
        ('1ere', '1ere'),
        ('Tale', 'Tale'),
    )

    annee = models.CharField(max_length=7, choices=evaluation_Preparation_classe, default='2nde', verbose_name="Classe")
    nom = models.ForeignKey(enseignant, on_delete=models.CASCADE, verbose_name="Enseignant responsable")
    candidat = models.ForeignKey(eleve, on_delete=models.CASCADE, verbose_name="candidat")
    chantier_a_evaluer = models.ForeignKey(attribution_d_un_chantier, on_delete=models.CASCADE,
                                           verbose_name="chantier à évaluer")
    heurePass = models.PositiveSmallIntegerField(verbose_name="Nombre d'heures passées")
    statut = models.CharField(max_length=35, choices=evaluation_Preparation_statut, default='Absent')
    tache_Preparation = models.ForeignKey(tacheP, on_delete=models.CASCADE, verbose_name="Tâche(s) validée(s)")
    competenceC1 = models.ForeignKey(competenceC1, on_delete=models.CASCADE, verbose_name="C1")
    competenceC2 = models.ForeignKey(competenceC2, on_delete=models.CASCADE, verbose_name="C2")
    competenceC3 = models.ForeignKey(competenceC3, on_delete=models.CASCADE, verbose_name="C3")
    competenceC10 = models.ForeignKey(competenceC10, on_delete=models.CASCADE, verbose_name="C10")
    competenceC11 = models.ForeignKey(competenceC11, on_delete=models.CASCADE, verbose_name="C11")
    competenceC12 = models.ForeignKey(competenceC12, on_delete=models.CASCADE, verbose_name="C12")
    attitude_Preparation = models.ForeignKey(attitude, on_delete=models.CASCADE,
                                             verbose_name="attitude(s) professionnelle(s) acquise(s)")
    appreciation = models.CharField(max_length=150, verbose_name="Appréciation")
    Note = models.PositiveSmallIntegerField(verbose_name="Note proposée /20")

    def __unicode__(self):
        return u"{0} {1}: {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9} - {10} - {11} - {12} - {13} - {14}/20 - {15}h ".format(
            self.annee, self.chantier_a_evaluer.electricien,
            self.chantier_a_evaluer.date, self.chantier_a_evaluer.travail_eleve, self.chantier_a_evaluer.Nb_heure,
            self.tache_Preparation.tache_1_1,
            self.tache_Preparation.tache_1_2, self.tache_Preparation.tache_1_3, self.tache_Preparation.tache_1_4,
            self.competenceC1.C1, self.competenceC2.C2, self.competenceC3.C3,
            self.competenceC10.C10, self.competenceC11.C11, self.competenceC12.C12, self.attitude_Preparation.attitude1,
            self.attitude_Preparation.attitude2, self.statut, self.appreciation, self.Note, self.nom.nom,
            self.heurePass)


# evaluation MISE EN SERVICE

class evaluation_Mise_en_service(models.Model):
    evaluation_Mise_en_service_statut = (
        ('Mise en service terminee', 'Mise en service terminee'),
        ('Terminee hors delai', 'Terminee hors delai'),
        ('Stoppe', 'Stoppe'),
        ('Absent', 'Absent'),
    )
    evaluation_Mise_en_service_classe = (
        ('2nde', '2nde'),
        ('1ere', '1ere'),
        ('Tale', 'Tale'),
    )

    annee = models.CharField(max_length=7, choices=evaluation_Mise_en_service_classe, default='2nde',
                             verbose_name="Classe")
    nom = models.ForeignKey(enseignant, on_delete=models.CASCADE, verbose_name="Enseignant responsable")
    candidat = models.ForeignKey(eleve, on_delete=models.CASCADE, verbose_name="candidat")
    chantier_a_evaluer = models.ForeignKey(attribution_d_un_chantier, on_delete=models.CASCADE,
                                           verbose_name="chantier à évaluer")
    statut = models.CharField(max_length=35, choices=evaluation_Mise_en_service_statut, default='Absent')
    heurePass = models.PositiveSmallIntegerField(verbose_name="Nombre d'heures passées")
    tache_Mise_en_service = models.ForeignKey(tacheMi, on_delete=models.CASCADE, verbose_name="Tâche(s) validée(s)")
    competenceC2 = models.ForeignKey(competenceC2, on_delete=models.CASCADE, verbose_name="C2")
    competenceC5 = models.ForeignKey(competenceC5, on_delete=models.CASCADE, verbose_name="C5")
    competenceC6 = models.ForeignKey(competenceC6, on_delete=models.CASCADE, verbose_name="C6")
    competenceC7 = models.ForeignKey(competenceC7, on_delete=models.CASCADE, verbose_name="C7")
    competenceC8 = models.ForeignKey(competenceC8, on_delete=models.CASCADE, verbose_name="C8")
    competenceC9 = models.ForeignKey(competenceC9, on_delete=models.CASCADE, verbose_name="C9")
    competenceC10 = models.ForeignKey(competenceC10, on_delete=models.CASCADE, verbose_name="C10")
    attitude_Mise_en_service = models.ForeignKey(attitude, on_delete=models.CASCADE,
                                                 verbose_name="attitude(s) professionnelle(s) acquise(s)")
    appreciation = models.CharField(max_length=150, verbose_name="Appréciation")
    Note = models.PositiveSmallIntegerField(verbose_name="Note proposée /20")

    def __unicode__(self):
        return u"{0} {1}: {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9} - {10} - {11} - {12} - {13}/20 - {14}h ".format(
            self.annee,
            self.chantier_a_evaluer.electricien, self.chantier_a_evaluer.date, self.chantier_a_evaluer.travail_eleve,
            self.chantier_a_evaluer.Nb_heure,
            self.tache_Mise_en_service.tache_3_1, self.tache_Mise_en_service.tache_3_2, self.competenceC2.C2,
            self.competenceC5.C5, self.competenceC6.C6, self.competenceC7.C7,
            self.competenceC8.C8, self.competenceC9.C9, self.competenceC10.C10, self.attitude_Mise_en_service.attitude1,
            self.attitude_Mise_en_service.attitude2, self.statut,
            self.appreciation, self.Note, self.nom.nom, self.heurePass)


# evaluation MAINTENANCE

class evaluation_Maintenance(models.Model):
    evaluation_Maintenance_statut = (
        ('Maintenance terminee', 'Maintenance terminee'),
        ('Terminee hors delai', 'Terminee hors delai'),
        ('Stoppe', 'Stoppe'),
        ('Absent', 'Absent'),
    )
    evaluation_Maintenance_classe = (
        ('2nde', '2nde'),
        ('1ere', '1ere'),
        ('Tale', 'Tale'),
    )

    annee = models.CharField(max_length=7, choices=evaluation_Maintenance_classe, default='2nde', verbose_name="Classe")
    nom = models.ForeignKey(enseignant, on_delete=models.CASCADE, verbose_name="Enseignant responsable")
    candidat = models.ForeignKey(eleve, on_delete=models.CASCADE, verbose_name="candidat")
    chantier_a_evaluer = models.ForeignKey(attribution_d_un_chantier, on_delete=models.CASCADE,
                                           verbose_name="chantier à évaluer")
    heurePass = models.PositiveSmallIntegerField(verbose_name="Nombre d'heures passées")
    statut = models.CharField(max_length=35, choices=evaluation_Maintenance_statut, default='Absent')
    tache_Maintenance = models.ForeignKey(tacheMa, on_delete=models.CASCADE, verbose_name="Tâche(s) validée(s)")
    competenceC2 = models.ForeignKey(competenceC2, on_delete=models.CASCADE, verbose_name="C2")
    competenceC5 = models.ForeignKey(competenceC5, on_delete=models.CASCADE, verbose_name="C5")
    competenceC6 = models.ForeignKey(competenceC6, on_delete=models.CASCADE, verbose_name="C6")
    competenceC7 = models.ForeignKey(competenceC7, on_delete=models.CASCADE, verbose_name="C7")
    competenceC8 = models.ForeignKey(competenceC8, on_delete=models.CASCADE, verbose_name="C8")
    competenceC9 = models.ForeignKey(competenceC9, on_delete=models.CASCADE, verbose_name="C9")
    competenceC10 = models.ForeignKey(competenceC10, on_delete=models.CASCADE, verbose_name="C10")
    attitude_Maintenance = models.ForeignKey(attitude, on_delete=models.CASCADE,
                                             verbose_name="attitude(s) professionnelle(s) acquise(s)")
    appreciation = models.CharField(max_length=150, verbose_name="Appréciation")
    Note = models.PositiveSmallIntegerField(verbose_name="Note proposée /20")

    def __unicode__(self):
        return u"{0} {1}: {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9} - {10} - {11} - {12} - {13} - {14}/20 - {15}h ".format(
            self.annee,
            self.chantier_a_evaluer.electricien, self.chantier_a_evaluer.date, self.chantier_a_evaluer.travail_eleve,
            self.chantier_a_evaluer.Nb_heure,
            self.tache_Maintenance.tache_4_1, self.tache_Maintenance.tache_4_2, self.competenceC2.C2,
            self.competenceC5.C5, self.competenceC6.C6, self.competenceC7.C7,
            self.competenceC8.C8, self.competenceC9.C9, self.competenceC10.C10, self.attitude_Maintenance.attitude1,
            self.attitude_Maintenance.attitude2, self.statut,
            self.appreciation, self.Note, self.nom.nom, self.heurePass)


# evaluation COMMUNICATION

class evaluation_Communication(models.Model):
    evaluation_Communication_statut = (
        ('Dossier chantier complet', 'Dossier chantier complet'),
        ('Dossier chantier incomplet', 'Dossier chantier complet'),
        ('Non rendu', 'Non rendu'),
        ('Absent', 'Absent'),
    )
    evaluation_Communication_classe = (
        ('2nde', '2nde'),
        ('1ere', '1ere'),
        ('Tale', 'Tale'),
    )

    annee = models.CharField(max_length=7, choices=evaluation_Communication_classe, default='2nde',
                             verbose_name="Classe")
    nom = models.ForeignKey(enseignant, on_delete=models.CASCADE, verbose_name="Enseignant responsable")
    candidat = models.ForeignKey(eleve, on_delete=models.CASCADE, verbose_name="candidat")
    chantier_a_evaluer = models.ForeignKey(attribution_d_un_chantier, on_delete=models.CASCADE,
                                           verbose_name="chantier à évaluer")
    heurePass = models.PositiveSmallIntegerField(verbose_name="Nombre d'heures passées")
    statut = models.CharField(max_length=35, choices=evaluation_Communication_statut, default='Absent')
    tache_Communication = models.ForeignKey(tacheC, on_delete=models.CASCADE, verbose_name="Tâche(s) validée(s)")
    competenceC1 = models.ForeignKey(competenceC1, on_delete=models.CASCADE, verbose_name="C1")
    competenceC10 = models.ForeignKey(competenceC10, on_delete=models.CASCADE, verbose_name="C10")
    competenceC11 = models.ForeignKey(competenceC11, on_delete=models.CASCADE, verbose_name="C11")
    competenceC12 = models.ForeignKey(competenceC12, on_delete=models.CASCADE, verbose_name="C12")
    competenceC13 = models.ForeignKey(competenceC13, on_delete=models.CASCADE, verbose_name="C13")
    attitude_Communication = models.ForeignKey(attitude, on_delete=models.CASCADE,
                                               verbose_name="attitude(s) professionnelle(s) acquise(s)")
    appreciation = models.CharField(max_length=150, verbose_name="Appréciation")
    Note = models.PositiveSmallIntegerField(verbose_name="Note proposée /20")

    def __unicode__(self):
        return u"{0} {1}: {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9} - {10} - {11} - {12} - {13} - {14}/20 - {15}h ".format(
            self.annee,
            self.chantier_a_evaluer.electricien, self.chantier_a_evaluer.date, self.chantier_a_evaluer.travail_eleve,
            self.chantier_a_evaluer.Nb_heure,
            self.tache_Communication.tache_5_1, self.tache_Communication.tache_5_2, self.tache_Communication.tache_5_3,
            self.competenceC1.C1, self.competenceC10.C10,
            self.competenceC11.C11, self.competenceC12.C12, self.competenceC13.C13,
            self.attitude_Communication.attitude1, self.attitude_Communication.attitude2, self.statut,
            self.appreciation, self.Note, self.nom.nom, self.heurePass)
