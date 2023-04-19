import sys
"""Taille d’une chaîne
Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.
"""

def len_list():
	including = True
	i = 0
	while including == True:
		try:
			list[i]
		except Exception as e:
			print("la longeur de la liste est ", i)
			including = False
		finally:
			i += 1

		
if __name__ == "__main__":
	list = sys.argv[1]
	len_list()

		