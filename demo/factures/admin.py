from django.contrib import admin
from .models import Facture, Client  # Assurez-vous que le chemin est correct

class FactureAdmin(admin.ModelAdmin):
    list_display = ('numero', 'description', 'montant', 'date_creation', 'est_payee', 'client')  # Mettez à jour avec les bons champs
    search_fields = ('client__nom', 'numero', 'description')  # Champs à rechercher

admin.site.register(Facture, FactureAdmin)
