import sys
"""L’alphabet à partir de
Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.
"""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
l =""
i = 0

while alphabet[i] != sys.argv[1]:
	i += 1

while i != 25:
	l += alphabet[i]
	i += 1
print(l)