
def parallelepipede(longueur, largeur, hauteur):
    longueur, largeur, hauteur = int(longueur), int(largeur), int(hauteur)
    print "le volume du parallelepipede est de : " + str(longueur*largeur*hauteur)

def time_convertor(number):
    seconds = int(number)
    minutes = seconds/60
    hours = minutes/24
    days = hours/24
    months = days/30
    years = months/12
    print "Number of seconds = " + str(seconds) + "\nNumber of minutes = " + str(minutes) + "\nNumber of days = " + str(days) + "\nNumber of months = " + str(months) + "\nNumber of years = " + str(years)
