class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print(f"Je suis: {self.nom} {self.prenom}")

personne1 = Personne("Nettah", "Caly")
personne1.SePresenter()

personne2 = Personne("Nettah", "Sohan")
personne2.SePresenter()