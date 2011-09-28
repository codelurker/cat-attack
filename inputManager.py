import pygame

class InputMgr:
	engine=None
	
	mousePos=(0,0)
	
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