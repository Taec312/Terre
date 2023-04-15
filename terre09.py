import sys
"""Racine carrée d’un nombre
Créez un programme qui affiche la racine carrée d’un entier positif.
val = int(sys.argv[1])
resultat = 0
i = 1
while resultat != val:
	i = i + 1
	resultat = i * i
	resultat = round(resultat)
print("la racine carré de ",sys.argv[1]," est de ",i) 

"""

def racineEntière():
	val = int(sys.argv[1])
	resultat = 0
	i = 1
	while resultat != val:
		i += 1
		if i*i == val:
			print(i)
			return 1
	print(i)

def i():
	val = int(sys.argv[1])
	resultat = 0
	i = 1
	if racineEntière():
		print("")
	else:
		while resultat != val and i < val :
			i += 0.01
			resultat = i * i
			resultat = round(resultat)
			print(i)
		print("la racine carré de ",sys.argv[1]," est de ",resultat) 

i()

