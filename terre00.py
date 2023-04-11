"""
L’alphabet
Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.
"""
l= ""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
taille = len(alphabet)-1
for i in range(taille):
	l += alphabet[i]
print(l)