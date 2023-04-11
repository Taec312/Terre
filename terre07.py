import sys
"""Taille d’une chaîne
Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.
"""
if len(sys.argv) != 2:
	print("erreur")
else:
	taille = len(sys.argv[1])
	print(taille)