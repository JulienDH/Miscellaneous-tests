class Domino(object):

    def __init__ (self,A = 0, B = 0):
        self.faceA = int(A)
        self.faceB = int(B)

    def affiche_points(self):
        print "Face A : " + str(self.faceA) + " Face B : " + str(self.faceB)

    def valeur(self):
        total = self.faceA + self.faceB
        print total

if __name__ == "__main__":
    firstDomino = Domino(2,3)
    firstDomino.affiche_points()
    firstDomino.valeur()
