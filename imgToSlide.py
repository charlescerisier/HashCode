import parse as p

H,V = p.parse('a_example.txt',2000)


def imgToSlide(listeV,listeH):
    nliste=[]
    j =0
    for i in range (0,len(listeV),2):
        h = {}
        h['id'] =j
        h['content']=[listeV[i],listeV[i+1]]
        nliste.append(h)
        j+=1
    for i in range (len(listeH)): 
        h = {}
        h['id'] =j
        h['content']=[listeH[i]]
        nliste.append(h)    
        j+=1
        
    return nliste

#imgtoSlide
if __name__ == "__main__":
    imgToSlide(H,V)

