from parse import *
from match import *
from imgToSlide import *
from slideByNbTags import *

def main():
	H, V = parse("c_memorable_moments.txt", 2000)
	slides = imgToSlide(H,V)
	slidesByNbTags = slidesByNbTags(slides)

if __name__ == "__main__":
	main()