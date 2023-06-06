from django.db import models

# Create your models here.
class Client(models.Model):
    """
        Informations de la table client
    """
    nomClient = models.CharField(max_length=40, verbose_name='Nom')
    prenomClient = models.CharField(max_length=50, verbose_name='Prenom ')
    adresseClient = models.CharField(max_length=60, verbose_name='Adresse')
    telClient = models.CharField(max_length=10, verbose_name='Contact ')

    def __str__(self):
        return self.nomClient
    
    objects = models.Manager()
    
class Appareil(models.Model):
    """
        Informations de la table Appareil
    """
    TYPE_APPAREIL = [
        ("Unite Cemtrale", "Unite Centrale"),
        ("Ordinateur Portable", "Ordinateur Portable"),
        ("Imprimante", "Imprimante"),
        ("Scanner", "Scanner")
    ]
    typeAppareil = models.CharField(max_length=50, choices=TYPE_APPAREIL, verbose_name='Type')
    marqueAppareil = models.CharField(max_length=20, verbose_name='Marque')
    dateArrAppareil = models.DateTimeField(auto_now=True, verbose_name='Date d\'Arriver')

    def __str__(self) -> str:
        return self.typeAppareil
    
class Technicien(models.Model):
    """
        Informations de la table Technicien
    """
    numTechnicien = models.CharField(max_length=5, verbose_name='Identifiant')
    nomTechnicien = models.CharField(max_length=40, verbose_name='Nom')
    prenomTechnicien = models.CharField(max_length=50, verbose_name='Prenom')
    specialiteTechnicien = models.CharField(max_length=20, verbose_name='Specialite')

    def __str__(self) -> str:
        return self.nomTechnicien

class Intervention(models.Model):
    """
        Informations de la table Intervention
    """
    typeIntervention = models.CharField(max_length=20, verbose_name='Type')
    problemeAppareil = models.CharField(max_length=100, verbose_name='Probleme')
    dateIntervention = models.DateField(auto_now=True, verbose_name='Date')
    appareil = models.ForeignKey(Appareil, on_delete=models.CASCADE, verbose_name="Appareil")
    technicien = models.ForeignKey(Technicien, on_delete=models.CASCADE, verbose_name="Technicien")

    def __str__(self) -> str:
        return self.typeIntervention
    
class Piece(models.Model):
    """
        Informations de la table Piece
    """
    refPiece = models.CharField(max_length=20, verbose_name='Reference')
    typePiece = models.CharField(max_length=20, verbose_name='Type')
    montantPiece = models.IntegerField(verbose_name='Montant')

    def __str__(self) -> str:
        return super().__str__()
    
class Utiliser(models.Model):
    """
        Informations de la table Utiliser
    """
    technicien = models.ForeignKey(Technicien, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    qtePiece = models.IntegerField(10)
    
class Reglement(models.Model):
    """
        Informations de la table Reglement
    """
    TYPE_REGLEMENT = [
        ("Espece", "Espece"),
        ("Virement Bancaire", "Virement Bancaire"),
        ("Cheque", "Cheque"),
        ("Transfert Monnaie", "Transfert Monnaie"),
    ]
    typeReglement = models.CharField(max_length=50, choices=TYPE_REGLEMENT, verbose_name='Type')
    dateReglement = models.DateTimeField(auto_now=True, verbose_name='Date')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client')
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE, verbose_name='Intervention')

    def __str__(self) -> str:
        return self.typeReglement