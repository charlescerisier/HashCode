# Retourne le score de l'image (0.5 = parfait)
def compare(listeA, listeB):	
	nbTags = len(listeA)
	count = 0
	for tag in listeA:
		if tag in listeB:
			count += 1
	
	return count/nbTags

# Retourne si le score entre 2 images est 0.5 à delta près
def match(delta, listeA, listeB):
	score = compare(listeA, listeB)
	return  (0.5 - delta <= score) and ( score <= 0.5 + delta)

if __name__ == "__main__":
	print(match(0.2, ['A', 'B', 'C', 'D', 'E', 'F'], ['F','A','D','E','H','I']))
	print(match(0.1, ['A', 'B', 'C', 'D', 'E', 'F'], ['A', 'B', 'C', 'D', 'E', 'F']))
	print(match(0.1, ['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L']))