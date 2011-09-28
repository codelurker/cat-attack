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

		#blit surface to screen
		self.screen.blit(self.screenBuffer, (0,0))
		pygame.display.flip()