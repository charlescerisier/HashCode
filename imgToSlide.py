import parse as p

#H,V = p.parse('a_example.txt',2000)


def imgToSlide(listeH,listeV):
    nliste=[]
    j =0
    for i in range (0,len(listeV),2):
        v = {}
        v['id'] =j
        v['content']=[listeV[i],listeV[i+1]]
        nliste.append(v)
        j+=1

    for i in range (len(listeH)): 
        h = {}
        h['id'] =j
        h['content']=[listeH[i]]
        nliste.append(h)    
        j+=1
        
    return nliste
