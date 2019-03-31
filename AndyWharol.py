import os.path
from PIL import Image as imag
from math import *
from random import randint

"""repertoire = "P:\\ISN\\IMAGES\\Python\\AndyWharol"
repertoireSauvegarde = "P:\\ISN\\IMAGES\\Python\\AndyWharol.png"
nomImg = "\\index.png"

if os.path.exists(repertoire):
	imageSource = img.open(repertoire + nomImg)
	LARGEUR, HAUTEUR = imageSource.size

	NLARGEUR = LARGEUR
	NHAUTEUR = HAUTEUR

	imageBuffer_fin = img.new("RGB", (NLARGEUR*3, NHAUTEUR*3))"""   

nomImage = "x.jpg"

imageSource = imag.open(nomImage)

LARGEUR, HAUTEUR = imageSource.size

NLARGEUR = LARGEUR
NHAUTEUR = HAUTEUR

imageBuffer_fin = imag.new("RGB", (NLARGEUR*3, NHAUTEUR*3))


listeImage = []

def permutation(img):
	global imageSource
	global LARGEUR
	global HAUTEUR

	imageBuffer = imag.new("RGB", (NLARGEUR, NHAUTEUR))

	for x in range(LARGEUR):
		for y in range(HAUTEUR):
			p = img.getpixel((x,y))
			p1 = (p[2], p[0], p[1])
			imageBuffer.putpixel((x, y),p1)

	return imageBuffer

def permutation2(img):
	global imageSource
	global LARGEUR
	global HAUTEUR

	imageBuffer = imag.new("RGB", (NLARGEUR, NHAUTEUR))

	for x in range(LARGEUR):
		for y in range(HAUTEUR):
			p = img.getpixel((x,y))
			p1 = (p[1], p[2], p[0])
			imageBuffer.putpixel((x, y),p1)

	return imageBuffer


def inversion(img):
	global imageSource
	global LARGEUR
	global HAUTEUR

	imageBuffer = imag.new("RGB", (NLARGEUR, NHAUTEUR))

	for x in range(LARGEUR):
		for y in range(HAUTEUR):
			p = img.getpixel((x,y))
			p1 = (255-p[0], 255-p[1], 255-p[2])
			imageBuffer.putpixel((x, y),p1)

	return imageBuffer


def gris(img):
	global imageSource
	global LARGEUR
	global HAUTEUR

	imageBuffer = imag.new("RGB", (NLARGEUR, NHAUTEUR))

	for x in range(LARGEUR):
		for y in range(HAUTEUR):
			p = img.getpixel((x,y))
			ng = int((p[0]+p[1]+p[2])/3)
			ng1 = (ng,ng,ng)
			imageBuffer.putpixel((x, y),ng1)

	return imageBuffer


def inversion2(img):
	#global imageSource
	global LARGEUR
	global HAUTEUR

	imageBuffer = imag.new("RGB", (NLARGEUR, NHAUTEUR))

	for x in range(LARGEUR):
		for y in range(HAUTEUR):
			p = img.getpixel((x,y))
			p1 = (255-p[0], 255-p[1], 255-p[2])
			imageBuffer.putpixel((x, y),p1)

	return imageBuffer


def retirerComposante(Compo,img):

	global imageSource
	global LARGEUR
	global HAUTEUR

	imageBuffer = imag.new("RGB", (NLARGEUR, NHAUTEUR))

	for x in range(LARGEUR):
		for y in range(HAUTEUR):
			p = img.getpixel((x,y))
			if Compo == "R" :
				p1 = (0, p[1], p[2])
			elif Compo == "G" :
				p1 = (p[0], 0, p[2])
			elif Compo == "B" :
				p1 = (p[0], p[1], 0)
			else :
				print("probleme")

			imageBuffer.putpixel((x, y),p1)

	return imageBuffer

				

"""def pixelBlanc(p,x,y):

	if (p[0] >= 240 and p[0] <= 255) and (p[1] >= 240 and p[1] <= 255) and (p[1] >= 240 and p[1] <= 255):
		p = (randint(0,255),randint(0,255),randint(0,255))
	else :
		pass

	return p	"""


imageBuffer1 = imageSource
imageBuffer2 = permutation(imageSource)
imageBuffer3 = permutation2(imageSource)
imageBuffer4 = inversion(imageSource)
imageBuffer5 = gris(imageSource)
imageBuffer6 = inversion2(imageBuffer5)
imageBuffer7 = retirerComposante("R",imageSource)
imageBuffer8 = retirerComposante("G",imageSource)
imageBuffer9 = retirerComposante("B",imageSource)

listeImage.append(imageBuffer1)
listeImage.append(imageBuffer2)
listeImage.append(imageBuffer3)
listeImage.append(imageBuffer4)
listeImage.append(imageBuffer5)
listeImage.append(imageBuffer6)
listeImage.append(imageBuffer7)
listeImage.append(imageBuffer8)
listeImage.append(imageBuffer9)

n = 0
m = 0

i = 0

while n < 3 and m < 3 :

	for x in range(LARGEUR):
		for y in range(HAUTEUR):
			p = listeImage[i].getpixel((x,y))
			#p = pixelBlanc(p,x,y)

			imageBuffer_fin.putpixel((x+n*LARGEUR, y+m*HAUTEUR), p)
	
	i += 1

	if m != 3 :
		if n == 2 :
			n = 0
			m += 1 
		else :
			n += 1
	else :
		break


imageBuffer_fin.save("C:\\Users\\Christophe W\\Desktop\\"+nomImage.replace(".jpg","(1).jpg"))
imageBuffer_fin.show()		











