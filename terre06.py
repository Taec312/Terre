import sys
"""Inverser une chaîne
Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.
"""
def reverse_chain():      #chaine inversé
	liste = ""
	position = len(arg)-1
	t= len(arg)

	for i in range(t):
		liste += arg[position]
		position -= 1

	print(liste)

if __name__ == "__main__":
	arg = sys.argv[1]
	reverse_chain()