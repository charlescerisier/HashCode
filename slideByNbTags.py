def slidesByNbTags(slides, delta = 0) :
	listeByNbTags = []
	
	taille = 1
	while len(slides) > 0 :
		tab = []
		for slide in slides : # On parcourt toutes les slides restantes
			nbTags = 0
			for img in slide['content'] :
				nbTags += img['nbTags']

			if (nbTags <= taille + delta) and (nbTags >= taille - delta) :
				tab.append(slide)
				#print("-----------\n{}\n".format(slides))
				slides.pop(slides.index(slide))
				#print("{}-----------\n".format(slides))

		listeByNbTags.append(tab)
		taille+=1

	newListeByNbTags = []
	
	for tab in listeByNbTags:
		#print(tab)
		if tab != []:
			newListeByNbTags.append(tab)

	return newListeByNbTags

if __name__ == "__main__":
	slides = []
	slidesByNbTags(slides, 0)
