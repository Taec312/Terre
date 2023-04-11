import sys
"""Inverser une chaîne
Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.
"""
l = sys.argv[1]
liste = ""
taille = len(l)-2

for i in range(taille):
	liste += l[taille]
	taille -= 1

print(liste)