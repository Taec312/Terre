import sys
"""Trié ou pas
Créez un programme qui détermine si une liste d’entiers est triée ou pas
"""
"""
if len(sys.argv[1]) != 1:  
	print("erreur.")
"""
taille = len(sys.argv)-1								#le nom du fichier compte 
i = 1
val = 0
if sys.argv[1].isdigit() != True and taille+1 == 2:	
	print("erreur.")
	val = 1
else:
	if int(sys.argv[1]) < int(sys.argv[2]):
		while i <= taille-1: 
			if int(sys.argv[i]) > int(sys.argv[i+1]):		#par de i = 0 -> nom du fichier
				print("Pas triée !")
				val = 1
				break
			else:
				i += 1
	else:
		if int(sys.argv[1]) > int(sys.argv[2]):
			while i <= taille-1:
				if int(sys.argv[i]) < int(sys.argv[i+1]):
					print("Pas triée !")
					val = 1
					break
				else:
					i += 1
		
if val == 0:
	print("triée !")