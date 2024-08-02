class Voiture:
    def __init__(self):
        self.couleur=''
        self.marque=""
        self.modele=''
    
    def Afficher(self):
        print(f"Couleur :{self.couleur}, Marque : {self.marque}, Modele : {self.modele}")


class Toyota(Voiture):
    def __init__(self):
        self.annee=''



rav= Toyota()
rav.annee='2022'
rav.couleur='rouge'
rav.marque='New Model'
rav.modele='RAV4'
rav.Afficher()


