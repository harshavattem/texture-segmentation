import os, os.path
import cv2
import random
import numpy as np
from PIL import Image

DIR='Textures'
num_images=len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name)) and name.split('.')[-1]=='jpg'])
num_images -=10
imgset = set()
while len(imgset) < 16:
    imgset.add(random.randint(1,num_images-1))
imgset = list(imgset)


img = []
for i in range (16):
	image = Image.open(DIR+'/D'+str(imgset[i])+'.jpg')
	#temp_image=cv2.imread(DIR+'/D'+str(imgset[i])+'.jpg', 0)
	box = (256,256,384,384)
	crop = image.crop(box)
	crop.save("temp.png","PNG")
	img.append(cv2.imread('temp.png', 0))
																																																																																																																																			
    
x_length=len(img[0])
y_length=len(img[0][0])


mosaic=[]

for x in range(y_length*4) :
    mosaic.append(np.zeros((x_length*4)))
    
for x in range (4):
    img_id = 4*x
    y_add = x * y_length
    for y in range (4):
        x_add = y * x_length
        for i in range (x_length):
            for j in range (y_length):
                mosaic[x_add+i][y_add + j] = img[img_id][i][j]
        img_id+=1    
    
mosaic = np.array(mosaic, dtype = np.uint8)

#cv2.imshow('image', mosaic)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite('mosaic.png', mosaic)






