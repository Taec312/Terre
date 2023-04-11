import sys
"""12 to 24
Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.
"""
if sys.argv[1][5] == "P":
	h = sys.argv[1].split(":")
	h1 = int(h[0]) 
	h1 += 12
	m = h[1].split("P")
	
else:
	h = sys.argv[1].split(":")
	m = h[1].split("A")
	print(str(h[0])+ ":"+ str(m[0]) )

