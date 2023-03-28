
class Rectangle:
    def __init__(self, longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur
        
    def get_longeur(self):
        return self.__longeur
    def get_largeur(self):
        return self.__largeur
    
    def set_longeur(self, longeur):
        self.__longeur = longeur
    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle1 = Rectangle(10,5)

print("Longeur: ", rectangle1.get_longeur())
print("Largeur:", rectangle1.get_largeur())

rectangle1.set_longeur(20)
rectangle1.set_largeur(10)

print("la nouvelle longeur est:", rectangle1.get_longeur())
print("la nouvelle largeur est:", rectangle1.get_largeur())