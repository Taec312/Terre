import sys
"""
Nom du programme
Créez un programme qui affiche son nom de fichier.
"""
def name_file():
	print(name)

if __name__ == "__main__":
	name = sys.argv[0]
	name_file()