import sys
"""Divisions
Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres
"""
x = int(sys.argv[1]) 
y = int(sys.argv[2])
if x >= y:
	resultat = x // y
	reste = x % y
	print("resultat: ",resultat)
	print("reste: ",reste)
else:
	print("erreur")
