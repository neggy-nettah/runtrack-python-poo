class Forme:
    def __init__(self):
        pass
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        Forme.__init__(self)
        
    def aire(self):
        return (self.radius ** 2) * 2
    
cercle = Cercle(30)
print(cercle.aire()) 
        