def concatenateSlides(matrixOfSlides):

	listOfSlides = []
	
	for eachList in matrixOfSlides :
		for eachSlide in eachList :
			listOfSlides.append(eachSlide)
	
	return listOfSlides


def fromSlidesToResponse(fileName, listOfSlides):

	listOfImgs = []
	nbSlides = len(listOfSlides)
	ret = "\n"
	esp = " "

	file = open(fileName+".response","w+")
	file.write(str(nbSlides) + ret)

	for eachSlide in listOfSlides :
		for eachImg in eachSlide["content"] :
			file.write(str(eachImg["ID"]) + esp)
		file.write(ret)

	return listOfImgs