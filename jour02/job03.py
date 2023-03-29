class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
        
    def perimetre(self):
        return 2 * (self._longueur + self._largeur)
        
    def surface(self):
        return self._longueur * self._largeur
        
    def get_longueur(self):
        return self._longueur
    
    def set_longueur(self, longueur):
        self._longueur = longueur
        
    def get_largeur(self):
        return self._largeur
    
    def set_largeur(self, largeur):
        self._largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
        
    def volume(self):
        return self._longueur * self._largeur * self._hauteur
    
    def get_hauteur(self):
        return self._hauteur
    
    def set_hauteur(self, hauteur):
        self._hauteur = hauteur

rectangle = Rectangle(10, 5)
print(rectangle.perimetre())  # output: 30
print(rectangle.surface())  # output: 50

parallelepipede = Parallelepipede(10, 5, 3)
print(parallelepipede.perimetre())  # output: 30
print(parallelepipede.surface())  # output: 50
print(parallelepipede.volume())  # output: 150
