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

#Input manager class- informs engine of what the user is doing with his keyboard/mouse

import pygame

class InputMgr:
	engine=None
	
	mousePos=(0,0) #we store the position of the mouse when it is clicked
	
	mouseClicked=False
	quit=False
	
	def __init__(self, engine):
		self.engine=engine
		
	def step(self):	
		self.mouseClicked=False
		self.quit=False

		for event in pygame.event.get():
			if (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: 
				self.quit=True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.mouseClicked=True
				self.mousePos=event.pos
				
	def shouldQuit(self):
		return self.quit
		
	def isMouseClicked(self):
		return self.mouseClicked
				
	def getMousePos(self):
		return self.mousePos