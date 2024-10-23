from django.shortcuts import render, get_object_or_404, redirect
from .models import Facture, Categorie, Client
from .forms import FactureForm, CategorieForm, ClientForm

def creer_facture(request):
    if request.method == 'POST':
        print('here')
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save(commit=False)
            if not facture.categorie:
                autres, created = Categorie.objects.get_or_create(nom="Autres")
                facture.categorie = autres
            facture.save()
            return redirect('liste_factures')
    else:
        form = FactureForm()
    return render(request, 'factures/creer_facture.html', {'form': form})

def modifier_facture(request, id):
    facture = get_object_or_404(Facture, id=id)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('liste_factures')
    else:
        form = FactureForm(instance=facture)
    return render(request, 'factures/modifier_facture.html', {'form': form})

def supprimer_facture(request, id):
    facture = get_object_or_404(Facture, id=id)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')
    return render(request, 'factures/supprimer_facture.html', {'facture': facture})

def liste_factures(request):
    client_id = request.GET.get('client_id')
    categorie_id = request.GET.get('categorie_id')
    
    min_montant = request.GET.get('min_montant')
    max_montant = request.GET.get('max_montant')

    factures = Facture.objects.all()
    clients = Client.objects.all()
    categories = Categorie.objects.all()

    if client_id:
        factures = factures.filter(client_id=client_id)

    if min_montant:
        factures = factures.filter(montant__gte=min_montant)
    if max_montant:
        factures = factures.filter(montant__lte=max_montant)

    if categorie_id:
        factures = factures.filter(categorie_id=categorie_id)

    return render(request, 'factures/liste_factures.html', {'factures': factures, 'clients': clients, 'categories': categories})



def ajouter_categorie(request):
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarder la nouvelle catégorie
            return redirect('liste_factures')  # Redirection après l'ajout, modifie selon ton projet
    else:
        form = CategorieForm()
    
    return render(request, 'factures/ajouter_categorie.html', {'form': form})

def ajouter_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarder le nouveau client
            return redirect('liste_factures')  # Redirection après l'ajout
    else:
        form = ClientForm()
    
    return render(request, 'factures/ajouter_client.html', {'form': form})

def liste_clients(request):
    clients = Client.objects.all()  # Récupérer tous les clients
    return render(request, 'factures/liste_clients.html', {'clients': clients})


def index(request):
    return render(request, 'factures/index.html')