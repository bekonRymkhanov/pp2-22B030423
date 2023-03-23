import os
listofmusic=list(os.walk("C:/Users/User/Desktop/python/music"))
for path,dirs,files in listofmusic:
    for file in files:
        pathed=os.path.join("C:/Users/User/Desktop/python/music",file)
        print(pathed)