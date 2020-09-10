class deque:
	'''a ordered strcuture that allows items to be added and removed from both its front (F) and rear (R)'''
	def __init__(self):
		self.items = []
	
	def addFront(self, x):
		self.items.insert(0, x)

	def addFront(self, x):
		self.items.append(x)
	
	def removeFront(self, x):
		if len(self.items) == 0:
			return None
		item = self.items[0]
		del self.items[0]
		return item

	def removeRear(self, x):
		if len(self.items) == 0:
			return Nones
		return self.items.pop()
	
	def __len__(self):
		return len(self.items)
	
	def __repr__(self):
		return str(self.items)