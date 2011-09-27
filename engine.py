import constants

class Engine:
	cats=[]
	level=1
	score=0
	
	def __init__(self):
		self.graphicsRenderer= renderer.Renderer(self)
		self.inputMgr= inputManager.InputMgr(self)
		self.soundPlayer= soundPlayer.SoundPlayer(self)
		
		self.loadCats(level)
		
	def mainLoop(self):
		quit=False
		while not quit:
	