import sys
"""24 to 12
Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.
"""
def clock_conversion():
	heure = sys.argv[1].split(":")
	h = int(heure[0])
	if h > 12:
		h = h - 12
		print(str(h)+":"+heure[1],"PM")		#, met un espace pas le + 
	else:
		print(sys.argv[1],"AM")

if __name__ == "__main__":
	clock_conversion()