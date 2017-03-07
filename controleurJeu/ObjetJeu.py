import Object

#Classe abstraite ObjetJeu
class ObjetJeu:
    def estPierre():
        return false

    def estFeuille():
        return false

    def estCiseau():
        return false

    #Méthode de comparaison, si ce qu'on renvoie est supérieur à 0
    #alors l'objet sur lequel on appelle la méthode gagne
    #Si ce qu'on renvoie est inférieur à 0 alors l'obejt sur lequel on appelle
    #la méthode perd.
    #S'il sont de même type on renvoie 0
    def gagne(o):
        if(self.estPierre()==o.estPierre() or self.estCiseau()==o.estCiseau() or self.estFeuille()==o.estFeuille):
            return 0

        elif(self.estPierre()):
            if(o.estCiseau()):
                return 1
            elif(o.estFeuille()):
                return -1

        elif(self.estFeuille()):
            if(o.estPierre()):
                return 1
            elif(o.estCiseau()):
                return -1

        elif(self.estCiseau()):
            if(o.estPierre()):
                return -1
            elif(o.estFeuille()):
                return 1
