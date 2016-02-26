#coding=utf-8

from random import *
import sys

class JeuDeCartes():

    joueur1_points = 0
    joueur2_points = 0

    def __init__(self):
        self.liste = []
        for i in range(0,4):
            for j in range(2,15):
                self.liste.append((j,i))

    def nom_carte(self, (numero,couleur)):
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
            #self.carte = self.nom_carte(self.liste[0])
            self.indice = self.liste[0]
            self.liste.remove(self.liste[0])
            return self.indice



if __name__ == "__main__":

    def gagnant(carte1,carte2):
        num1 = carte1[0]
        num2 = carte2[0]
        if (num1 > num2):
            print "Joueur 1 gagne cette manche. Il a mtn " + str(joueur1_points) + " points"
            joueur1_points = joueur1_points + 1
        elif (num1 < num2):
            joueur2_points = joueur2_points + 1
            print "Joueur 2 gagne cette manche. Il a mtn " + str(joueur1_points) + " points"
        elif (num1 == num2):
            print "Match nul pour cette manche."
        if joueur1_points > 27:
            print "Fin de la partie. Le joueur1 a gagné avec " + str(joueur1_points) + " points"
            sys.exit()
        if joueur2_points > 27:
            print "Fin de la partie. Le joueur2 a gagné" + str(joueur2_points) + " points"
            sys.exit()

    joueur1_points = 0
    joueur2_points = 0
    joueur1 = JeuDeCartes()
    joueur1.battre()
    joueur2 = JeuDeCartes()
    joueur2.battre()

    for i in range(2):
        carte1 = joueur1.tirer()
        num1 = carte1[0]
        carte2 = joueur2.tirer()
        num2 = carte2[0]
        print ("Le joueur 1 vient de tirer un :"), joueur1.nom_carte(carte1)
        print ("Le joueur 2 vient de tirer un :"), joueur2.nom_carte(carte2)
        gagnant(carte1,carte2);
