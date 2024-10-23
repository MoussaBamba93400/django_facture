from django.urls import path
from . import views

urlpatterns = [
    path('factures/', views.liste_factures, name='liste_factures'),
    path('factures/creer/', views.creer_facture, name='creer_facture'),
    path('factures/modifier/<int:id>/', views.modifier_facture, name='modifier_facture'),
    path('factures/supprimer/<int:id>/', views.supprimer_facture, name='supprimer_facture'),
    path('ajouter-categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('ajouter-client/', views.ajouter_client, name='ajouter_client'),
    path('clients/', views.liste_clients, name='liste_clients'),
]
