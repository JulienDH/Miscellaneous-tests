#coding=utf-8

from random import *

class JeuDeCartes():

    def __init__(self):
        self.liste = []
        for i in range(0,4):
            for j in range(2,15):
                self.liste.append((j,i))

    def nom_carte(self, numero, couleur):
        self.numero = int(numero)
        self.couleur = int(couleur)

        if self.couleur == 0:
            self.couleur = str("Coeur")
        elif self.couleur == 1:
            self.couleur = str("Carreau")
        elif self.couleur == 2:
            self.couleur = str("Trèfle")
        elif self.couleur == 3:
            self.couleur = str("Pique")

        if self.numero == 11:
            self.numero = str("Vallet")
        elif self.numero == 12:
            self.numero = str("Roi")
        elif self.numero == 13:
            self.numero = str("Reine")
        elif self.numero == 14:
            self.numero = str("As")

        print str(self.numero) + " de " + self.couleur

    def battre(self):
        for i in self.liste:
            a = randint(0, 51)
            b = randint(0, 51)
            temp = self.liste[a]
            self.liste[a] = self.liste[b]
            self.liste[b] = temp

    def tirer(self):
        if (len(self.liste) == 0):
            print "Jeu terminé !"
        else:
            self.carte = self.liste[0]
            self.nom_carte(self.carte[0],self.carte[1])
            self.liste.remove(self.carte)


if __name__ == "__main__":

    joueur1 = JeuDeCartes()
    joueur1.battre()
    joueur2 = JeuDeCartes()
    joueur2.battre()

    for i in range(52):
        print "Le joueur 1 vient de tirer un :" + joueur1.tirer()
        print "Le joueur 1 vient de tirer un :" + joueur2.tirer()
