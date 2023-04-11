import sys
"""Pair ou impair
Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
"""
x = int(sys.argv[1])
 
if x < 0:
	print("Tu ne me la mettras pas à l’envers.")
elif x % 2 == 0:
	print("pair")
else:
	print("impair")