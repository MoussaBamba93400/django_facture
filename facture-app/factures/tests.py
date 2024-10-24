from django.test import TestCase
from .models import Facture, Categorie, Client

class CategorieModelTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Services")

    def test_categorie_creation(self):
        self.assertEqual(self.categorie.nom, "Services")
    
    def test_categorie_str_method(self):
        self.assertEqual(str(self.categorie), "Services")


class ClientModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(nom="John Doe", email="johndoe@example.com")

    def test_client_creation(self):
        self.assertEqual(self.client.nom, "John Doe")
        self.assertEqual(self.client.email, "johndoe@example.com")
    
    def test_client_str_method(self):
        self.assertEqual(str(self.client), "John Doe")


class FactureModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(nom="Jane Smith", email="janesmith@example.com")
        self.categorie = Categorie.objects.create(nom="Consulting")

        self.facture = Facture.objects.create(
            numero="F001",
            description="Facture for consulting services",
            montant=1000.00,
            categorie=self.categorie,
            client=self.client,
            est_payee=False
        )

    def test_facture_creation(self):
        self.assertEqual(self.facture.numero, "F001")
        self.assertEqual(self.facture.description, "Facture for consulting services")
        self.assertEqual(self.facture.montant, 1000.00)
        self.assertFalse(self.facture.est_payee)
        self.assertEqual(self.facture.categorie.nom, "Consulting")
        self.assertEqual(self.facture.client.nom, "Jane Smith")

    def test_facture_str_method(self):
        self.assertEqual(str(self.facture), "F001")
