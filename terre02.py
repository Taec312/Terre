import sys
"""
Nom du programme
Créez un programme qui affiche son nom de fichier.
"""
taille = len(sys.argv)-1

for i in range(taille):
	print(sys.argv[i+1])

