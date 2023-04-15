import sys
"""Puissance d’un nombre
Créez un programme qui affiche le résultat d’une puissance.
L’exposant ne pourra pas être négatif.

def power():
	global y				 #global?
	for i in range(x-1):
		y = y* y	
	print(y)

def main():
	if len(sys.argv) == 3 and x>=0:
		power()
	else:
		print("attention ton exposant est peux être negatif ")

if __name__ == "__main__":
	y = int(sys.argv[1])
	x = int(sys.argv[2])
	power()
"""
def power():
	result = y
	for i in range(x-1):
		result = result* y	
	print(result)

def main():
	if len(sys.argv) == 3 and x>=0:
		power()
	else:
		print("attention ton exposant est peux être negatif ")

if __name__ == "__main__":
	y = int(sys.argv[1])
	x = int(sys.argv[2])
	power()