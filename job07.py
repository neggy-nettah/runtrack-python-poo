
class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = int(pages)
    
    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur
        
    def get_pages(self):
        return self.__pages
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")
    

livre1 = Livre("Amazing" , "toto", 200.5)

print("Titre:", livre1.get_titre(),'\n' "Auteur:", livre1.get_auteur(),'\n' "Nombres de pages:", livre1.get_pages())
