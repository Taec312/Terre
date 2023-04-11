import sys
"""Puissance d’un nombre
Créez un programme qui affiche le résultat d’une puissance.
L’exposant ne pourra pas être négatif.
"""
y = int(sys.argv[1])
x = int(sys.argv[2])
res = 0
if len(sys.argv) == 3 and x>=0:
	
	for i in range(x-1):
		res += y * y
	print(res)

else:
	print("attention ton exposant est peux être negatif ")
