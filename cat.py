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
	
	hitBoxSize=200
	
	def __init__(self, engine):
		self.engine=engine
		
		self.posX= random.randrange(0, SCREEN_WIDTH)
		self.posX= random.randrange(0, SCREEN_HEIGHT)

		self.rotation=random.randrange(0,360)
		
		self.speedX=random.randrange(-10*self.engine.level,10*self.engine.level)
		self.speedY=random.randrange(-10*self.engine.level,10*self.engine.level)
		
		#Uncomment this line for unoptimized resource management (along with the one further down)
		self.surface= pygame.image.load("ada.png")
		
	def step(self):
		self.posX+= self.speedX
		self.posY+= self.speedY
		
		if self.posX<0 or self.posX>SCREEN_WIDTH:
			self.speedX*=-1

		if self.posY<0 or self.posY>SCREEN_HEIGHT:
			self.speedY*=-1
		
		#Uncomment the 3 following lines for rotation
		self.rotation+=1
		self.rotation= self.rotation%360
		self.tmpSurface=pygame.transform.rotate(self.surface,self.rotation) #always rotate the source surface, not a rotated surface!
		
	def getSurface(self):
		#Uncomment this line for optimized resource management
		#return self.engine.resourceMgr.getResource("ada.png")
		
		#Or uncomment this for unoptimized resource management
		return self.surface
		
		#Or uncomment this along with the 3 rotation lines if you want spinny cats
		#return self.tmpSurface
		
	def getBlitPos(self):
		return (self.posX, self.posY)
		
	def isClicked(self, (x, y)):
		if x>self.posX and x<(self.posX+self.hitBoxSize):
			if y>self.posY and y<(self.posY+self.hitBoxSize):
				return True
		return False