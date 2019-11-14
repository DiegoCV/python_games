class Cuadro():
	"""docstring for Cuadro"""
	def __init__(self, x, y):		
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def aumentarY(self, y):
		self.y += y