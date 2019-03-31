import pygame
import os
from random import *
from math import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

imageEnnemi = pygame.image.load("Ennemi.png")
imageJoueur = pygame.image.load("Joueur.png")
imageMur = pygame.image.load("Mur.png")
imageEspaceVide = pygame.image.load("EspaceVide.png")
imageCacherTexte = pygame.image.load("MurPourCacherTexte.png")

nomFont = "Earth 2.0.0.80.ttf"
mafont = pygame.font.Font(nomFont, 20)
texteCollision = mafont.render("Vous ne pourvez pas franchir de murs ! ", True, (0,0,0))

HAUTEUR,LARGEUR = 400,640
DIMENSION = (LARGEUR,HAUTEUR)

listeDesMurs = list()
listeDesEnnemis = list()

nombreDeToursBouclePrincipale = 0

Map_1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,
         0,0,0,2,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,
         0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,
         0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,
         0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	

'''class Ennemi():

	def __init__(self, x, y, debutYVeloPosi, debutYVeloNega, debutXVeloPosi, debutXVeloNega):
		self.image = imageEnnemi
		self.largeur, self.hauteur = self.image.get_size()	

		self.x = x
		self.y = y 

		self.debutXVeloNega = debutXVeloNega
		self.debutXVeloPosi = debutXVeloPosi
		self.debutYVeloNega = debutYVeloNega
		self.debutYVeloPosi = debutYVeloPosi

		self.coordonnees = (self.x, self.y)

		self.velociteDirection = "bas"

		self.yVelocite = 4
		self.xVelocite = 4

	def setVeloDirection(self):
		if self.coordonnees == self.debutYVeloPosi :
			self.velociteDirection = "bas"
			print(velociteDirection)
		if self.coordonnees == self.debutXVeloPosi :
			self.velociteDirection = "droite"
			print("lol")
		if self.coordonnees == self.debutYVeloNega :
			self.velociteDirection = "haut"
			print("ptdr")
		if self.coordonnees == self.debutXVeloNega :
			self.velociteDirection = "gauche"
			print("mdr")
		else :
			pass

	def afficher(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def updatePos(self):
		if self.velociteDirection == "bas" :
			self.y += self.yVelocite
			
		elif self.velociteDirection == "droite" :
			self.x += self.xVelocite
			
		elif self.velociteDirection == "haut" :
			self.y -= self.yVelocite
			
		elif self.velociteDirection == "gauche" :
			self.x -= self.xVelocite
			
		else :
			pass'''						

class Mur():
	def __init__(self,x,y):
		self.image = imageMur
		self.largeur, self.hauteur = self.image.get_size()

		self.x = x
		self.y = y	

	def afficher(self, screen):
		screen.blit(self.image, (self.x, self.y))	

class Joueur():

	def __init__(self, x, y):

		self.x = x
		self.y = y
		self.xVelocite = 0
		self.yVelocite = 0

		self.image = imageJoueur

		self.largeur, self.hauteur = self.image.get_size()

	def afficher(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def updatePos(self):
		self.x += self.xVelocite
		self.y += self.yVelocite

	def enCollision(self, objet):

		if self.x < objet.x + objet.largeur and self.x + self.largeur > objet.x :
			if self.y < objet.y + objet.hauteur and self.y + self.hauteur > objet.y :
				return True
			else :
				return False
		else :
			return False						

def creeMap(mapChoisie, screen):

	numeroColonne = 0
	numeroLigne = 0

	screen.fill((255,255,255))

	for point in mapChoisie :
		if point == 0 : 
			pass
			numeroColonne += 1
			if numeroColonne == 40 :
				numeroLigne += 1
				numeroColonne = 0 
		if point == 1 :
			screen.blit(imageEnnemi, (numeroColonne*16, numeroLigne*16)) 
			numeroColonne += 1 
			if numeroColonne == 40 :
				numeroLigne += 1
				numeroColonne = 0
		if point == 2 :
			mur = Mur(numeroColonne*16, numeroLigne*16)
			listeDesMurs.append(mur)	
			numeroColonne += 1
			if numeroColonne == 40 :
				numeroLigne += 1
				numeroColonne = 0
		if point == 3 : 
			xJoueur, yJoueur = numeroColonne*16, numeroLigne*16
			numeroColonne += 1
			if numeroColonne == 40 :
				numeroLigne += 1 
				numeroColonne = 0

	return xJoueur, yJoueur			



def quitter():
	pygame.quit()
	quit()

def main():

	global nombreDeToursBouclePrincipale

	#listeDesEnnemis.append(Ennemi(8, 8, (8,8), (8,16), (0,0), (0,0)))

	screen = pygame.display.set_mode(DIMENSION)

	xJ, yJ = creeMap(Map_1, screen)

	joueur = Joueur(xJ, yJ)

	screen.blit(texteCollision, (180, 2))

	while True :

		clock.tick(FPS)

		if nombreDeToursBouclePrincipale >= 1:
			screen.blit(imageEspaceVide, (joueur.x, joueur.y))	

		for event in pygame.event.get():
			if event.type == pygame.QUIT : 
				quitter()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_UP :
					joueur.yVelocite = -4
				if event.key == pygame.K_DOWN :
					joueur.yVelocite = 4
				if event.key == pygame.K_LEFT :
					joueur.xVelocite = -4
				if event.key == pygame.K_RIGHT :
					joueur.xVelocite = 4
			elif event.type == pygame.KEYUP :
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
					joueur.yVelocite = 0  	
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
					joueur.xVelocite = 0 

		#xJ, yJ = creeMap(Map_1, screen)

		joueurEnCollision = False
		
		for mur in listeDesMurs :
			mur.afficher(screen)
			if joueur.enCollision(mur) == False :
				pass
			elif mur.x + 4 == joueur.x + joueur.largeur :
				joueur.x -= 4
				#screen.blit(texteCollision, (180, 2))
			elif mur.x + mur.largeur - 4 == joueur.x :
				joueur.x += 4
				#screen.blit(texteCollision, (180, 2))
			elif joueur.y == mur.y + mur.hauteur - 4 :
				joueur.y += 4
				#screen.blit(texteCollision, (180, 2))
			elif joueur.y + joueur.hauteur == mur.y + 4 :
				joueur.y -= 4
				#screen.blit(texteCollision, (180, 2))			 
			else :
				joueurEnCollision = True

		if joueurEnCollision == False :				
			joueur.updatePos()
		else :
			pass

		

		joueur.afficher(screen)
		pygame.display.update()	
		nombreDeToursBouclePrincipale += 1			
	
		

main()	
