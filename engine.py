from constants import *

import renderer
import inputManager
import soundPlayer
import resourceManager
import cat
import time

class Engine:
	cats=[]
	level=1
	score=0
	
	frameStart=0
	lastFrameCalculationTime=0
	fps=0
	lastFPSSum=0
	
	def __init__(self):
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

			if (len(self.cats)==0):
				self.level+=1
				self.loadCats(self.level)
				print "Level up!"
				print len(self.cats)

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
			