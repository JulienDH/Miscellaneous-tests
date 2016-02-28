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

def rise(max):
    liste = [1]
    for i in xrange(0,max):
        liste.append(liste[i]*2)
    return liste[max]

def letter_count(word, letter):
    i = 0
    for element in word:
        if element == letter:
            i+=1
    print 'The letter: {} found {} time' .format(letter, i)

def insert_star(word):
    new_word = ""
    for letter in word:
        new_word = new_word + letter + "*"
    return new_word

def palindrome(word):
    new_word = ""
    for letter in word:
        new_word = letter + new_word
    if word ==  new_word:
        print "Oui c'est un palindrome"
    else:
        print "Non ce n'est pas un palindrome"

def top_nbr():
    liste = [132, 5, 12, 8, 3, 75, 2, 85]
    biggest = liste[0]
    length = len(liste)
    i = 0
    while i <= length-1:
        if liste[i] > biggest:
            biggest = liste[i]
        i+=1
    print 'The largest number is {}' .format(biggest)

def pair_impair():
    liste = [132, 5, 12, 8, 3, 75, 2, 85]
    length = len(liste)
    even = []
    odd = []
    i = 0
    while i <= length-1:
        if liste[i]%2==0:
            even.append(liste[i])
        else:
            odd.append(liste[i])
        i+=1
    print "Even elements:\n" + str(even) + "\nOdd elements:\n" + str(odd)
