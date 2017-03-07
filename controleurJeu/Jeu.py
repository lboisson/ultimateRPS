"""import Object
import ObjetJeu
import Pierre
import Ciseau
import Feuille"""

#Classe abstraite ObjetJeu
class ObjetJeu:
    def estPierre(self):
        return False

    def estFeuille(self):
        return False

    def estCiseau(self):
        return False

    #Méthode de comparaison, si ce qu'on renvoie est supérieur à 0
    #alors l'objet sur lequel on appelle la méthode gagne
    #Si ce qu'on renvoie est inférieur à 0 alors l'obejt sur lequel on appelle
    #la méthode perd.
    #S'il sont de même type on renvoie 0
    def gagne(self, o):
        """if(self.estPierre==(o.estPierre==True) or self.estCiseau==(o.estCiseau==True) or self.estFeuille==(o.estFeuille==True)):
            return 0"""

        if(self.estPierre()):
            if(o.estCiseau()):
                return 1
            elif(o.estFeuille()):
                return -1
            else:
                return 0

        elif(self.estFeuille()):
            if(o.estPierre):
                return 1
            elif(o.estCiseau()):
                return -1
            else:
                return 0

        elif(self.estCiseau()):
            if(o.estPierre()):
                return -1
            elif(o.estFeuille()):
                return 1
            else:
                return 0

        else:
            print("Erreur de comparaison")
            return -666

#Classe correspondant au Ciseau
class Ciseau(ObjetJeu):
    def estCiseau(self):
        return True

#Classe correspondant à la Feuille
class Feuille(ObjetJeu):
    def estFeuille(self):
        return True

#Classe correspondant à la pierre
class Pierre(ObjetJeu):
    def estPierre(self):
        return True

def main():
    joueur1=Pierre()
    joueur2=Pierre()
    print(joueur1.gagne(joueur2))

main()
