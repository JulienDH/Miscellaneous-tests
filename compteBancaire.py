class CompteBancaire():

    def __init__ (self, name, solde):
        self.name = str(name)
        self.solde = int(solde)

    def depot(self, somme):
        self.depot = int(somme)
        self.nouveau_solde = self.solde + self.depot

    def retrait(self, somme):
        self.retrait = int(somme)
        self.nouveau_solde = self.solde - self.retrait

    def affiche(self):
        #self.solde_final = self.solde + self.solde_apres_depot - self.solde_apres_retrait

        print "Le solde du compte bancaire de " + str(self.name) +  " est de " + str(self.nouveau_solde) + " euros."
