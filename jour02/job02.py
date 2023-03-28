class Personne:
    def __init__(self, age=14):
        self.age = int(age)
        
    def afficherAge(self):
        print(f"L'âge de la personne est {self.age} ans")
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, nouvelAge):
        self.age = int(nouvelAge)

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print(f"J'ai {self.age} ans.")
        
class Professeur:
    def __init__(self, matiereEnseignee):
        self._matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer.")
    
    
personne = Personne()
eleve = Eleve()
professeur = Professeur("Francais")

eleve.affichageAge()
eleve.allerEnCours()

personne.afficherAge()
personne.bonjour()
personne.modifierAge(23)
personne.afficherAge()


professeur.enseigner()