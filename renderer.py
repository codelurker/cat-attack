class Renderer:
	engine=None
	
	
	def __init__(self, engine):
		self.engine=engine
		
	def render(self):
		#clear screen
		
		#render cats
		for cat in self.engine.cats:
			cat.blitTo(self.surface) 
		
		#render score
