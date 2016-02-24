class CompteBancaire():

    def __init__ (self, name = "Dupont", solde = 1000):
        self.name = str(name)
        self.solde = int(solde)

    def depot(self, somme = 0):
        self.depot = int(somme)
        self.solde = (self.solde + self.depot)

    def retrait(self, somme = 0):
        self.retrait = int(somme)
        self.solde = (self.solde - self.retrait)

    def affiche(self):
        print "Le solde du compte bancaire de " + str(self.name) +  " est de " + str(self.solde) + " euros."
