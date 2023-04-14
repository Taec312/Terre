import sys
"""
Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.
"""
size = len(sys.argv)-1
def display_argument():
	for i in range(size):
		print(sys.argv[i+1])

if __name__ == "__main__":
	display_argument()
