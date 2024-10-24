from django.urls import path
from . import views
from .views import FactureCreateView, FactureListView, CategorieCreateView, ClientCreateView, ClientList

urlpatterns = [
    path('factures/', FactureListView.as_view(), name='liste_factures'),
    path('factures/creer/', FactureCreateView.as_view(), name='creer_facture'),
    path('factures/modifier/<int:id>/', views.modifier_facture, name='modifier_facture'),
    path('factures/supprimer/<int:id>/', views.supprimer_facture, name='supprimer_facture'),
    path('ajouter-categorie/', CategorieCreateView.as_view(), name='ajouter_categorie'),
    path('ajouter-client/', ClientCreateView.as_view(), name='ajouter_client'),
    path('clients/', ClientList.as_view(), name='liste_clients'),
]
