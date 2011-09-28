import pygame

class ResourceManager:
	surfaces={}
	engine=None
	
	def __init__(self, engine):
		self.engine=engine
		
	def loadResource(self, resourceName, pathToResource):
		if (not resourceName in self.surfaces):
			self.surfaces[resourceName]= pygame.image.load(pathToResource)
		return self.surfaces[resourceName]