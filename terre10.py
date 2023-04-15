import sys
"""Nombre premier
Créez un programme qui affiche si un nombre est premier ou pas.
"""
def prime_number_test():
	if x == 0 or x == 1:
		return 0
	else:
		i = 2																	
		while i != x:
			if x % i == 0 and i != x: 
				
				return 0															
			else:
				i+= 1
	return 1				
	
def main():
	if prime_number_test():
		print("Oui ",sys.argv[1]," est un nombre premier.")
	else:
		print("Non ",sys.argv[1]," n'est pas un nombre premier." )

if __name__ == "__main__":
	x = int(sys.argv[1])
	main()