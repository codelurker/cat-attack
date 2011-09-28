import pygame

class ResourceManager:
	surfaces={}
	engine=None
	
	def __init__(self, engine):
		self.engine=engine
		
	def getResource(self, pathToResource):
		if (not pathToResource in self.surfaces):
			self.surfaces[pathToResource]= pygame.image.load(pathToResource)
		return self.surfaces[pathToResource]