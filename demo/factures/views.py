from django.shortcuts import render, get_object_or_404, redirect
from .models import Facture, Categorie, Client
from .forms import FactureForm, CategorieForm, ClientForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

class FactureCreateView(CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/creer_facture.html'
    success_url = reverse_lazy('liste_factures')

    def form_valid(self, form):
        facture = form.save(commit=False)
        if not facture.categorie:
            autres, created = Categorie.objects.get_or_create(nom="Autres")
            facture.categorie = autres
        facture.save()
        return super().form_valid(form)

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

class FactureListView(ListView):
    model = Facture
    template_name = 'factures/liste_factures.html'
    context_object_name = 'factures'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['categories'] = Categorie.objects.all()
        return context

    def get_queryset(self):
        factures = Facture.objects.all()
        client_id = self.request.GET.get('client_id')
        categorie_id = self.request.GET.get('categorie_id')
        min_montant = self.request.GET.get('min_montant')
        max_montant = self.request.GET.get('max_montant')

        if client_id:
            factures = factures.filter(client_id=client_id)
        if min_montant:
            factures = factures.filter(montant__gte=min_montant)
        if max_montant:
            factures = factures.filter(montant__lte=max_montant)
        if categorie_id:
            factures = factures.filter(categorie_id=categorie_id)

        return factures


class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'factures/ajouter_categorie.html'
    success_url = reverse_lazy('liste_factures')

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'factures/ajouter_client.html'
    success_url = reverse_lazy('liste_factures')

class ClientList(ListView):
    model = Client
    template_name = 'factures/liste_clients.html'
    context_object_name = 'clients'


def index(request):
    return render(request, 'factures/index.html')