import sys
"""Pair ou impair
Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
"""

def odd_or_even():			#doit t'on mettre number un argument de la fonction?
	if number < 0:
		print("Tu ne me la mettras pas à l’envers.")
	elif number % 2 == 0:
		print("even")
	else:
		print("odd")

if __name__ == "__main__":
	number = int(sys.argv[1])
	odd_or_even()
