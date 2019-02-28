def slidesByNbTags(slides, delta = 0) :
	listeByNbTags = []
	
	taille = 1
	while len(slides) > 0 :
		tab = []
		for slide in slides : # On parcourt toutes les slides restantes
			nbTags = 0
			for img in slide['content'] :
				nbTags += img['nbTags']

			if (nbTags >= taille + delta) or (nbTags >= taille - delta) :
				tab.append(slide)
				slides.pop(slide)
		listeByNbTags.append(tab)
		taille+=1

	return listeByNbTags

if __name__ == "__main__":
	slides = []
	slidesByNbTags(slides, 0)