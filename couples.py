from parse import *
from match import *

deltaIncrease = 0.005
ok = []
imgListMax = []

def giveFakeSlide (slide):
	if (len(slide['content']) == 2):
		#print(slide['content'][0]['tags'] + slide['content'][1]['tags'])
		return {'id': slide['id'], 'content': [{'ID': 0, 'type': 'H', 'nbTags': len(set(slide['content'][0]['tags'] + slide['content'][1]['tags'])), 'tags': set(slide['content'][0]['tags'] + slide['content'][1]['tags'])}]}
	else:
		return slide

def findCouples(ok, slideListMax, slideList, delta):

    if (len(slideList) > 1):
    
        slideRef = slideList[0]

        fakeSlide = giveFakeSlide(slideRef)

        slideListSearch = slideList.copy()
        slideListSearch.remove(slideRef)

        for slideSearch in slideListSearch:
            fakeSlideSearch = giveFakeSlide(slideSearch)

            if (match(delta, fakeSlide, fakeSlideSearch)):
                ok.append([slideRef, slideSearch])
                
                slideList.remove(slideSearch)
                slideList.remove(slideRef)

                print("Removing", slideRef['id'], "and", slideSearch['id'])
                print("Remaining slides :", len(slideListMax))

                return findCouples(ok, slideListMax, slideList, delta)

        return findCouples(ok, slideListMax, slideList, delta + deltaIncrease)

    else:
        return ok

if __name__ == "__main__":
    img = parse("c_memorable_moments.txt", 2000)[0]
    #print(img)
    findCouples([], img, img, 0)