
class Animal():
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom
        
    def vieillir(self): 
        print(f"L'age de l'animal est {self.age + 1} ans.")
        self.age += 1 # je ne sais pas ce qui est mieux et si jai bien compris la consigne surtout...
        print(f"L'age de l'animal est {self.age} ans.") 
    
    def nommer(self):
        print(f"L'animal se nomme {self.prenom}.")
    
animal1 = Animal(1, "luna")
animal1.vieillir()
animal1.nommer()