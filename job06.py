
class Rectangle:
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur
        
    def return_longeur(self):
        return self.longeur
    def return_largeur(self):
        return self.largeur
    
    def modif_longeur(self, longeur):
        self.longeur = longeur
    def modif_largeur(self, largeur):
        self.largeur = largeur

rectangle1 = Rectangle(10,5)

print("Longeur: ", rectangle1.return_longeur())
print("Largeur:", rectangle1.return_largeur())

rectangle1.modif_longeur(20)
rectangle1.modif_largeur(10)

print("la nouvelle longeur est:", rectangle1.return_longeur())
print("la nouvelle largeur est:", rectangle1.return_largeur())