#coding=utf-8

class Satellite():

    def __init__ (self, nom = '', masse = 100, vitesse = 0):
        self.nom = str(nom)
        self.masse = int(masse)
        self.vitesse = int(vitesse)

    def impulsion(self, force, duree):
        self.force = int(force)
        self.duree = int(duree)
        self.var_vitesse = ((self.force * self.duree)/self.masse)
        self.vitesse = self.vitesse + self.var_vitesse

    def affiche_vitesse(self):
        print "Vitesse du satellite " + self.nom + " = " + str(self.vitesse) + "m/s."

    def energie(self):
        en_cinetique = (0.5*(self.masse*(self.vitesse*self.vitesse)))
        return en_cinetique
