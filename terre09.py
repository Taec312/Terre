import sys
"""Racine carrée d’un nombre
Créez un programme qui affiche la racine carrée d’un entier positif.
val = int(sys.argv[1])
resultat = 0
i = 1
while resultat != val:
	i = i + 1
	resultat = i * i
	resultat = round(resultat)
print("la racine carré de ",sys.argv[1]," est de ",i) 

"""

def racineEntière():
	val = int(sys.argv[1])
	resultat = 0
	i = 1
	while resultat != val and i < val:
		if i*i == val:
			return i
		else:
			i += 1
	return 0

def Racine_pas_entière():	
		val = int(sys.argv[1])
		resultat = 0
		i = 1
		while resultat != val and i < val :
			i += 0.1
			resultat = i * i
			resultat = round(resultat)
		print("la racine carré de ",sys.argv[1]," est de ",i) 

def main():
	if racineEntière():
		print(racineEntière())
	else:
		Racine_pas_entière()

if __name__ == '__main__':
	main()


