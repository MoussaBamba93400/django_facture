from django import forms
from .models import Facture, Categorie, Client

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'description', 'montant', 'categorie', 'client', 'est_payee']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'email']