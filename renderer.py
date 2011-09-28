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

#Renderer class- in charge of rendering the game world on screen

from constants import *

import pygame

class Renderer:
	engine=None
	screenBuffer=None
	screen=None
	font=None
	
	def __init__(self, engine):
		self.engine=engine
		pygame.init()
		self.font=pygame.font.Font(None, 48)
		self.screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		#we render in an intermediary buffer that we then render on the screen- not useful in a basic case, but good practice.
		self.screenBuffer=pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		
	def render(self):
		#clear screen
		self.screenBuffer.fill((0,0,0))
		#render cats
		for cat in self.engine.cats:
			self.screenBuffer.blit(cat.getSurface(), cat.getBlitPos()) 
		
		#render score and level
		score=self.font.render('Score: '+str(self.engine.score), False, (255,255,255))
		self.screenBuffer.blit(score, (0,0))

		level=self.font.render('Level: '+str(self.engine.level), False, (255,255,255))
		self.screenBuffer.blit(level, (0,50))

		#blit screenbuffer to screen
		self.screen.blit(self.screenBuffer, (0,0))
		pygame.display.flip()