import sys
"""Divisions
Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres
"""
def division():
	if x >= y:
		result = x // y
		remainder = x % y
		print("result: ",result)
		print("remainder: ",remainder)
	else:
		print("erreur")

if __name__ == "__main__":
	x = int(sys.argv[1]) 
	y = int(sys.argv[2])
	division()
