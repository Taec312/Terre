import sys
"""Trouver la Suisse (lol)
Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.
"""
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
millieu = None 			
if x == y or x == z or y == z:
	print("Au moins 2 des valeurs sont identiques veuillez mettre 3 valeurs differents") #ou print("erreur")
elif (x < y and z < x) or (x < z and y < x):
	print("La valeur du millieu est: ",x)
elif (y < x and z < y) or (y < z and x < y):
	print("La valeur du millieu est: ",y)
else:
	print("La valeur du millieu est: ",z)