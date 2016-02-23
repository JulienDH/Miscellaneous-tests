import random

i = 0
lenght = 20
rank = -1

maListe = []
while i < lenght:
	maListe.append(random.randrange(0, 100, 1))
	i += 1

print "Ma liste initiale est :", maListe

for element in maListe:
	i = lenght - 1
	rank += 1
	while i >= 0:
		if maListe[rank] < maListe[lenght-1-i]:
			pivot = maListe[rank] 
			maListe[rank] = maListe[lenght-1-i]
			maListe[lenght-1-i] = pivot
		i -= 1
		
print "Ma liste triee est :", maListe
