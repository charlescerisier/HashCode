fileName = "a_example.txt"

nbPics = 0
pics = []
i = 0

# PICS LINE FORMAT
# PICS : 
# [
#    {
#       "nbTags": 1
#       "tags": ["tag1", "tag2", "tag3"]
#       "type": 'H'
#     }
# ]

with open(fileName) as file:
    print("File " + fileName + " opened")

    for line in file:
        print(line)
        if (i == 0):
            nbPics = line
        else:
            picLine = line.replace('\n', '').split(' ')
            pic = {}
            pic['type'] = picLine[0]
            pic['nbTags'] = picLine[1]
            pic['tags'] = picLine[2:]
            pics.append(pic)
        
        i += 1

    print(pics)