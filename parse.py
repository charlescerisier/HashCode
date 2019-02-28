def parse(fileName, maxTags) :
    nbPics = 0
    pics = []
    i = 0

    picsBySize = [[] for i in range(maxTags)]

    # PICS LINE FORMAT
    # PICS : 
    # [
    #    {
    #       "ID": 1
    #       "nbTags": 1
    #       "tags": ["tag1", "tag2", "tag3"]
    #       "type": 'H'
    #     }
    # ]

    with open(fileName) as file:
        print("File " + fileName + " opened")

        for line in file:
            #print(line)
            if (i == 0):
                nbPics = line.strip()
            else:
                picLine = line.strip().split(' ')
                pic = {}
                pic['ID'] = i - 1
                pic['type'] = picLine[0]
                pic['nbTags'] = int(picLine[1])
                pic['tags'] = picLine[2:]
                pics.append(pic)

                try:
                    picsBySize[int(picLine[1])].append(pic)
                except:
                    picsBySize[int(picLine[1])] = []
                    picsBySize[int(picLine[1])].append(pic)
            
            i += 1

        #print(pics)

    H = []
    V = []

    for pic in pics:
        if (pic['type'] == 'H'):
            H.append(pic)
        else:
            V.append(pic)

    print("Number of images : " + nbPics)
    print("H : " + str(len(H)) + " ; V : " + str(len(V)))

    return H,V

if __name__ == "__main__":
    parse("c_memorable_moments.txt", 2000)