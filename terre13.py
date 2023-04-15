import sys
"""Trouver la Suisse (lol)
Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.
"""

def middle_value():		
	if x == y or x == z or y == z:
		print("Au moins 2 des valeurs sont identiques veuillez mettre 3 valeurs differents") #ou print("erreur")
	elif (z < x < y) or (y < x < z):
		print("La valeur du millieu est: ",x)
	elif (z < y < x) or (x < y < z):
		print("La valeur du millieu est: ",y)
	else:
		print("La valeur du millieu est: ",z)

if __name__ == "__main__":
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	z = int(sys.argv[3])
	middle_value()