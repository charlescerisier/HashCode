from parse import *
from match import *
from imgToSlide import *
from slideByNbTags import *

def printSlide(slide):
	for key,val in slide.items():
		print("{} => {}".format(key, val))

def main():
	H, V = parse("c_memorable_moments.txt", 2000)
	slides = imgToSlide(H,V)

	printSlide(slides[0])
	print(len(slides))
	slidesSortedBySize = slidesByNbTags(slides[0:300])
	print(len(slidesSortedBySize))

if __name__ == "__main__":
	main()