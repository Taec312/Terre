import sys
"""L’alphabet à partir de
Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.
"""


def display_alphabet():
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	l =""
	i = 0
	
	while alphabet[i] != letter:
		i += 1

	while i != 25:
		l += alphabet[i]
		i += 1
	print(l)

if __name__ == "__main__":
	letter = sys.argv[1]
	display_alphabet()