#coding=utf-8

def parallelepipede(length, width, height):
    #Calculate the parallelepipoid volume
    length, width, height = int(length), int(width), int(height)
    print "le volume du parallelepipede est de : " + str(length*width*height)

def time_convertor(number):
    #seconds conversion
    seconds = int(number)
    minutes = seconds/60
    hours = minutes/24
    days = hours/24
    months = days/30
    years = months/12
    print "Number of seconds = " + str(seconds) + "\nNumber of minutes = " + str(minutes) + "\nNumber of days = " + str(days) + "\nNumber of months = " + str(months) + "\nNumber of years = " + str(years)

def multiple(number):
    #Create a list of number multiple of the args
    #After each number modulo 3, a * is inserted
    liste = []
    for i in range(1,20):
        liste.append(i*number)
    for element in liste:
        if element != "*" and (element%3 == 0):
            liste.insert(liste.index(element)+1,"*")
    return liste

def multi(number):
    #the shorter way of the multiple function
    for i in range(1,20):
        number = i*number
        print number,
        if number%3==0:
            print "*",

def picto(number):
    #draw a half fir tree
    for i in range(1,number):
        print i * "*"
