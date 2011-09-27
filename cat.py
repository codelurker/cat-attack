import pygame
import random

class Cat:
	surface=None
	rotation=0

	posX=0
	posY=0
	
	speedX=0
	speedY=0
	
	def __init__(self):
		self.posX= random.randrange(0, _SCREEN_WIDTH_)
		self.posX= random.randrange(0, _SCREEN_HEIGHT_)
		
		self.speedX=random.randrange(-10,10)
		self.speedY=random.randrange(-10,10)
		
		self.surface= pygame.image.load("ada.png")
		
	def tick(self):
		self.posX+= self.speedX
		self.posY+= self.speedY
		
		self.rotation+=1
		self.rotation= self.rotation%360
		
	def blitTo(self, surface):
		surface.blit(self.surface, (self.posX, self.posY))