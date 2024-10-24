from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Facture(models.Model):
    numero = models.CharField(max_length=50)
    description = models.TextField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    est_payee = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="factures")

    def __str__(self):
        return self.numero