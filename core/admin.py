from django import forms
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

from .models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nomClient', 'prenomClient', 'adresseClient', 'telClient')
    ordering = ('nomClient',)
    search_fields = ('nomClient', 'adresseClient')

@admin.register(Appareil)
class AppareilAdmin(admin.ModelAdmin):
    list_display = ('typeAppareil', 'marqueAppareil', 'dateArrAppareil')
    search_fields = ('typeAppareil', 'marqueAppareil')

@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('typeIntervention', 'problemeAppareil', 'dateIntervention', 'appareil', 'technicien')
    ordering = ('dateIntervention', )
    search_fields = ('appareil', 'dateIntervention')

@admin.register(Technicien)
class TechnicienAdmin(admin.ModelAdmin):
    list_display = ('numTechnicien', 'nomTechnicien', 'prenomTechnicien', 'specialiteTechnicien')
    search_fields = ('numTechnicien', 'nomTechnicien', 'specialiteTechnicien')

@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    list_display = ('refPiece', 'typePiece', 'montantPiece')
    search_fields = ('refPiece', 'typePiece')

@admin.register(Reglement)
class ReglementAdmin(admin.ModelAdmin):
    list_display = ('typeReglement', 'dateReglement', 'client', 'intervention')
    search_fields = ('typeReglement', 'dateReglement')

#Hide group in django admin panel

# Unregister the default GroupAdmin
admin.site.unregister(Group)