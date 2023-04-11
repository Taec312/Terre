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
val = int(sys.argv[1])
resultat = 0
i = 1
while resultat != val:
	i += 0.0000001
	resultat = i * i
	resultat = round(resultat)
print("la racine carré de ",sys.argv[1]," est de ",i) 