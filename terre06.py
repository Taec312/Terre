import sys
"""Inverser une chaîne
Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.
"""
l = sys.argv[1]
liste = ""
taille = len(l)-1
t= len(l)
print(taille)
print(t)
for i in range(t):
	liste += l[taille]
	taille -= 1

print(liste)