import sys
"""Nombre premier
Créez un programme qui affiche si un nombre est premier ou pas.
"""
x = int(sys.argv[1])
vrai = 1
if x == 0 or x == 1:
	print(sys.argv[1]," n'est pas un nombre premier.")
else:
	i = 2																	#tout les chiffre sont divisible par 1
	while i != x:
		if x % i == 0 and i != x: 
			print("Non ",sys.argv[1]," n'est pas un nombre premier." )
			vrai = 0
			break															#Sinon boucle a l'infini
		else:
			i+= 1					
	
	if vrai ==1:
		print("Oui ",sys.argv[1]," est un nombre premier.")