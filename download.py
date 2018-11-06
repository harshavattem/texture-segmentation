import requests

for i in range (1,150):
	
	url = 'http://www.ux.uis.no/~tranden/brodatz/D' + str(i) + '.gif'
	filename = 'Textures/' + url.split('/')[-1]
	try:
		r = requests.get(url, allow_redirects=True)
		open(filename, 'wb').write(r.content)
	except:
		pass
        
from PIL import Image
import os, os.path
import cv2 as cv
import random

DIR='Textures'
num_images=len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])


for name in [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]:
    if name.split('.')[-1] == 'gif':
        try:
            newname=os.path.join(DIR, name.rsplit('.',1)[0] + '.jpg')
            img = Image.open(os.path.join(DIR, name)).convert('L').save(newname)
            img = cv.imread(newname,0)
            img = img[0:640,0:640]
            cv.imwrite(newname,img)
        except IOError:
            os.remove(os.path.join(DIR, name))
