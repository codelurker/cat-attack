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

#Engine class- ties all components together and executes gameflow

from constants import *

import pygame
import renderer
import inputManager
import soundPlayer
import resourceManager
import cat
import time

class Engine:
	cats=[] #array holding all of the cat objects
	level=1
	score=0
	
	
	#These variables are used for framerate management
	frameStart=0
	lastFrameCalculationTime=0
	fps=0
	lastFPSSum=0
	
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Cat attack!")
		self.graphicsRenderer= renderer.Renderer(self)
		self.inputMgr= inputManager.InputMgr(self)
		self.soundPlayer= soundPlayer.SoundPlayer(self)
		self.resourceMgr= resourceManager.ResourceManager(self)
		
		self.loadCats(self.level)
		
	def mainLoop(self):
		quit=False

		while not quit:
			###
			self.frameStart=time.time()
			
			timeToSleep=(1./FRAME_PER_SECOND)-self.lastFrameCalculationTime
			if timeToSleep<0:
				timeToSleep=0
			time.sleep(timeToSleep)
			
			if (time.time()-self.lastFPSSum>1):
				print "FPS:", self.fps
				self.lastFPSSum=time.time()
				self.fps=0
			###
			
			self.inputMgr.step()

			#level up condition
			if (len(self.cats)==0):
				self.level+=1
				self.loadCats(self.level)

			for c in self.cats:
				c.step()
			
			if (self.inputMgr.isMouseClicked()):
				for c in self.cats:
					if c.isClicked(self.inputMgr.mousePos):
						self.score+=1
						self.cats.remove(c)
			
			self.graphicsRenderer.render()
			
			quit=self.inputMgr.shouldQuit()
			
			####
			self.lastFrameCalculationTime=time.time()-self.frameStart
			self.fps+=1
			#print "Frame render time:", self.lastFrameCalculationTime
			####
			
	def loadCats(self, level):
		
		for i in range(0,BASE_NUM_CATS+(5*self.level)):
			c=cat.Cat(self)
			self.cats.append(c)
			