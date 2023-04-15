import sys
"""Trié ou pas
Créez un programme qui détermine si une liste d’entiers est triée ou pas
"""
"""
if len(sys.argv[1]) != 1:  
	print("erreur.")
"""
def sort_or_not():
	taille = len(sys.argv)-1								#le nom du fichier compte 
	i = 1													#par de i = 0 -> nom du fichier
	first_number = int(sys.argv[1] )
	second_number = int(sys.argv[2] )												
	if first_number < second_number:
		while i <= taille-1: 
			if int(sys.argv[i]) > int(sys.argv[i+1]):		
				return 0
			else:
				i += 1
		return 1
	else:
		if first_number > second_number:
			while i <= taille-1:
				if int(sys.argv[i]) < int(sys.argv[i+1]):
					return 0
				else:
					i += 1
			return 1

def main():
	if sys.argv[1].isdigit() != True and taille+1 == 2:	
		print("erreur.")
	else:
		if sort_or_not():
			print("trié")
		else:
			print("Pas triée !")

if __name__ == '__main__':
	main()

	