from parse import *
from match import *
from imgToSlide import *
from slideByNbTags import *
from theEnd import *
from couples import *

def printSlide(slide):
	for key,val in slide.items():
		print("{} => {}".format(key, val))

def couplesSlidesToSlides(couples):
	slides = []
	for couple in couples:
		slides += couple[0]
		slides += couple[1]
	return slides

def main(fileNames):

	for fileName in fileNames:
		print("Processing " + fileName)
		H, V = parse(fileName, 2000)
		slides = imgToSlide(H,V)
		slidesSortedBySize = slidesByNbTags(slides)
		slides = concatenateSlides(slidesSortedBySize)
		final = couplesSlidesToSlides(findCouples([], slides, slides, 0 ))
		##print(len(slidesSortedBySize))
		fromSlidesToResponse(fileName, final)


if __name__ == "__main__":
	fileNames = ["c_memorable_moments.txt", "b_lovely_landscapes.txt", "d_pet_pictures.txt", "e_shiny_selfies.txt"]
	main(fileNames)