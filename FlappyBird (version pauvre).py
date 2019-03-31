import pygame
import os
from random import *

scoreJoueur = 0
#maPolice = pygame.font.SysFont(None, 14)
finDuGame = False

HAUTEUR,LARGEUR = 400,640
DIMENSION = (LARGEUR,HAUTEUR)
background = pygame.image.load("fondFlappy.png")
imagePerso  = pygame.image.load("flappyNinja.png")

tuyauBas = pygame.image.load("TuyauBas.png")
tuyauHaut = pygame.image.load("TuyauHaut.png")

screen = pygame.display.set_mode(DIMENSION)
pygame.display.set_caption("Flappy")

listeDesTuyaux = list()

espaceTuyau = 80
espaceXTuyaux = 230

clock = pygame.time.Clock()

def delTuyaux():

	global listeDesTuyaux

	i = 1 

	while i <= len(listeDesTuyaux) - 1:

		if listeDesTuyaux[i].x + listeDesTuyaux[i].largeurBas <= 0 :
			listeDesTuyaux.remove(listeDesTuyaux[i])	
		else :
			pass

		i += 1

class Joueur():

	def __init__(self, screen):
		
		self.screen = screen

		self.x = 50
		self.y = HAUTEUR/2


		self.yVelocite = 4

		self.image = imagePerso
		self.largeur, self.hauteur = self.image.get_size()
		self.largeur = self.largeur - 9 

		self.rectPerso = self.image.get_rect()

	def updatePos(self):
		
		self.y += self.yVelocite

	def afficher(self):

		screen.blit(self.image, (self.x, self.y))

	def horsEcran(self):
		if self.y < 0 :
			self.y = 0

		elif self.y > HAUTEUR - self.hauteur :
			self.y = HAUTEUR - self.hauteur 	

	def enCollisionAvec(self, tuyaux):
		if self.x + self.largeur >= tuyaux.x and self.x <= tuyaux.x + tuyaux.largeurBas:
			if self.y <= tuyaux.yTuyauHaut + tuyaux.hauteurHaut : 
				return True
			elif self.y + self.hauteur >= tuyaux.yTuyauBas :
				return True
			else : 
				return False				
							
class Tuyaux():

	def __init__(self) : 

		self.tuyauHaut = tuyauHaut
		self.tuyauBas = tuyauBas

		self.largeurBas, self.hauteurBas = self.tuyauBas.get_size()
		self.largeurHaut, self.hauteurHaut = self.tuyauHaut.get_size()

		self.rectTuyauxBas = self.tuyauBas.get_rect()
		self.rectTuyauxHaut = self.tuyauHaut.get_rect() 

		self.yTuyauBas = randrange(HAUTEUR/2, HAUTEUR - HAUTEUR/4)
		self.yTuyauHaut = self.yTuyauBas - espaceTuyau - self.hauteurHaut

		self.x = LARGEUR
		self.xVelocite = -5 + scoreJoueur*0.20

	def afficher(self, screen):

		screen.blit(self.tuyauBas, (self.x, self.yTuyauBas))
		screen.blit(self.tuyauHaut, (self.x, self.yTuyauHaut))

	def updatePos(self) :

		self.x += self.xVelocite		 

def quitter():
	pygame.quit()
	quit()

def gameOver():
	global finDuGame
	print("perdu !")
	finDuGame = True

def resetGame(joueurAReset):

	global listeDesTuyaux
	global finDuGame

	listeDesTuyaux = list()
	joueurAReset.yVelocite = 4
	joueurAReset.y = HAUTEUR/2
	tuyaux = Tuyaux()
	listeDesTuyaux.append(tuyaux)

	finDuGame = False

def main():

	global finDuGame

	joueur = Joueur(screen)
	tuyaux = Tuyaux()
	listeDesTuyaux.append(tuyaux)

	while True :

		if finDuGame == False :

			clock.tick(60)

			for event in pygame.event.get() :

				if event.type == pygame.QUIT : 
					quitter()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE :
						joueur.yVelocite = -3

				if event.type == pygame.KEYUP : 

					if event.key == pygame.K_SPACE :
						joueur.yVelocite = 3


			for tuyaux in listeDesTuyaux : 
				if listeDesTuyaux[len(listeDesTuyaux)-1].x <= LARGEUR - espaceXTuyaux :
					listeDesTuyaux.append(Tuyaux())
					

			screen.blit(background,(0,0))	

			for tuyaux in listeDesTuyaux : 
				tuyaux.afficher(screen)
				tuyaux.updatePos()
			
			delTuyaux()	

			for tuyaux in listeDesTuyaux :	
				if joueur.enCollisionAvec(tuyaux) == True :
					gameOver()
				else :
					pass 		     		


			joueur.updatePos()
			joueur.afficher()

			joueur.horsEcran() 
				
			pygame.display.update()

		
		elif finDuGame == True :

			screen.blit(background, (0,0))
			joueur.afficher()
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT :
					quitter()
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_ESCAPE :
						quitter()
					if event.key == pygame.K_r:
						resetGame(joueur)		


main()				
