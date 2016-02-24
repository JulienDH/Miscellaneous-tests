#coding=utf-8

class Voiture():

    def __init__(self, marque = 'Ford', couleur = 'rouge', nom = 'personne', vitesse = 0):
        self.marque = str(marque)
        self.couleur = str(couleur)
        self.nom = str(nom)
        self.vitesse = int(0)

    def choix_conducteur(self, nom = 'personne'):
        self.nom = str(nom)

    def accelerer(self, taux = 0, duree = 0):
        if self.nom != 'personne':
            self.vitesse = float(taux) * float(duree)
        else:
            print "Cette voiture n'a pas de conducteur."

    def affiche_tout(self):
        print self.marque + ", " + self.couleur + " pilotée par " + self.nom + ", vitesse = " + str(self.vitesse) + "m/s."
