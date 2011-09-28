from constants import *

import pygame
import random

class Cat:
	engine=None
	
	surface=None
	tmpSurface=None
	rotation=0

	posX=0
	posY=0
	
	speedX=0
	speedY=0
	
	def __init__(self, engine):
		self.engine=engine
		
		self.posX= random.randrange(0, SCREEN_WIDTH)
		self.posX= random.randrange(0, SCREEN_HEIGHT)

		self.rotation=random.randrange(0,360)
		
		self.speedX=random.randrange(-10*self.engine.level,10*self.engine.level)
		self.speedY=random.randrange(-10*self.engine.level,10*self.engine.level)
		
		#self.surface= pygame.image.load("ada.png")
		self.surface= self.engine.resourceMgr.loadResource("cat", "ada.png")
		
	def step(self):
		self.posX+= self.speedX
		self.posY+= self.speedY
		
		if self.posX<0 or self.posX>SCREEN_WIDTH:
			self.speedX*=-1

		if self.posY<0 or self.posY>SCREEN_HEIGHT:
			self.speedY*=-1
		
		self.rotation+=1
		self.rotation= self.rotation%360
		self.tmpSurface=pygame.transform.rotate(self.surface,self.rotation) #always rotate the source surface, not a rotated surface!
		
	def getSurface(self):
		return self.tmpSurface
		
	def getBlitPos(self):
		return (self.posX, self.posY)
		
	def isClicked(self, (x, y)):
		if x>self.posX and x<(self.posX+self.surface.get_width()):
			if y>self.posY and y<(self.posY+self.surface.get_height()):
				return True
		return False