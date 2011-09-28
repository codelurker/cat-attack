##############################################################################
#The MIT License

#Copyright (c) 2011 Guillaume Ardaud

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
##############################################################################

#Cat class- represents a class entity on screen

from constants import *

import pygame
import random

class Cat:
	engine=None #reference to the engine
	
	surface=None #holds the surface (used when we're using unoptimized resource management)
	tmpSurface=None #holds the rotated surface (for when we're making the cats spin)
	rotation=0 #rotation, in degrees

	posX=0 #x coordinate on screen
	posY=0 #y coordinate on screen
	
	speedX=0 #x speed in pixels per frame
	speedY=0 #y speed in pixels per frame
	
	hitBoxSize=200 #side of the clickable square zone
	
	def __init__(self, engine):
		self.engine=engine
		
		self.posX= random.randrange(0, SCREEN_WIDTH)
		self.posX= random.randrange(0, SCREEN_HEIGHT)

		self.rotation=random.randrange(0,360)
		
		self.speedX=random.randrange(-10*self.engine.level,10*self.engine.level) #speed increases with level
		self.speedY=random.randrange(-10*self.engine.level,10*self.engine.level)
		
		#Uncomment this line for unoptimized resource management (along with the one further down)
		self.surface= pygame.image.load("ada.png")
		
	def step(self):
		self.posX+= self.speedX
		self.posY+= self.speedY
		
		if self.posX<0 or self.posX>SCREEN_WIDTH: #make the cat bounce horizontally
			self.speedX*=-1

		if self.posY<0 or self.posY>SCREEN_HEIGHT: #make the cat bounce vertically
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
		#basic geometry here- we're checking whether the click has landed in the cat's hitbox or not
		if x>self.posX and x<(self.posX+self.hitBoxSize):
			if y>self.posY and y<(self.posY+self.hitBoxSize):
				self.engine.soundPlayer.playSound("meow.wav")
				return True
		return False