#coding=utf-8

import math

class Cercle():

    def __init__(self, rayon = 0):
        self.rayon = rayon

    def surface(self):
        return float(math.pi * (self.rayon**2))

class Cylindre(Cercle):

    def __init__(self, rayon = 0, hauteur = 0): #Arg nécessaires pour le fonctionnement de la class Cylindre
        Cercle.__init__(self, rayon) #Arg nécéssaires à la class Cercle
        self.hauteur = hauteur

    def volume(self):
        return self.surface()*self.hauteur

class Cone(Cylindre):

    def __init__(self, rayon = 0, hauteur = 0): #Arg nécessaires pour le fonctionnement de la class Cone
        Cylindre.__init__(self, rayon = 0, hauteur = 0) # Arg nécéssaire à la class Cylindre
        self.rayon = rayon
        self.hauteur = hauteur

    def volume(self):
        return Cylindre.volume(self)/3
