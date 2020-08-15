import math

class linkedListNode:
	'''a node in a linked list, with both a key and a value'''
	def __init__(self, key, value):
		self.key = key 
		self.val = value
		self.next = None

class linkedList:
	'''Linked list of key-value pairs, key is unique to list and appending a key that is already in the list overrides the value
	use linkedList[X] to get value asscoiated with key X
	use linkedList[X] = Val to add key X with value = Val
	'''
	def __init__(self):
		self.headVal = None
	
	def __setitem__(self, key, value):
		if self.headVal == None:
			#this is the first node
			self.headVal = linkedListNode(key, value)
		else:
			node = self.headVal
			while True:
				#is this current node using the key?
				if node.key == key:
					node.val = value #overwrite the value
					break
				#Move to next node if it exists, and if it doesnt, add a new node
				if node.next == None:
					node.next = linkedListNode(key, value)
					break
				else:
					node = node.next
		
	def __getitem__(self, key):
		'''find a key in the linked list, return the value'''
		node = self.headVal
		while True:
			if node.key == key:
				#match found
				return node.val
			elif node.next == None:
				return None
			else:
				node = node.next
	
	def __repr__(self):
		LIST = ""
		node = self.headVal
		while True:
			LIST += str((node.key, node.val)) 
			node = node.next
			if node == None:
				break
		return str(LIST)

class GrantDict:
	def __init__(self, initialContents = None, m = 1979):
		#init access table as a list
		self.m = m
		self.accessTable = [None for i in range(m)]
		#Parse any initial values
		if type(initialContents) == list and type(initialContents[0]) == tuple:
			for pair in initialContents:
				if len(pair) != 2:
					raise ValueError('GrantDict takes a list of tuples of length 2, or a single tuple. Tuple of length {0} recieved'.format(len(pair)))
				else:
					self.__setitem__(pair[0], pair[1])
		elif type(initialContents) == tuple:
			if len(initialContents) != 2:
				raise ValueError('GrantDict takes a list of tuples of length 2, or a single tuple. Tuple of length {0} recieved'.format(len(initialContents)))
			else:
				self.__setitem__(initialContents[0], initialContents[1])
		elif initialContents != None:
			raise ValueError('GrantDict takes a list of tuples of length 2, or a single tuple. {0} recieved'.format(type(initialContents)))		
	
	def __setitem__(self, key, value):
		'''key can be a int or string, value can take any form'''
		hashedKey = self.GrantHash(key)
		if self.accessTable[hashedKey] == None:
			self.accessTable[hashedKey] = linkedList()
			self.accessTable[hashedKey][key] = value
		else:
			self.accessTable[hashedKey][key] = value
			
	def __getitem__(self, key):
		'''use special class func __getitem__ to allow for GrantDictObj[Key] syntax to search dict'''
		hashedKey = self.GrantHash(key)
		return self.accessTable[hashedKey][key]
	
	def __repr__(self):
		outstr = ""
		for item in self.accessTable:
			if item != None:
				outstr += str(item)
		return outstr

	def GrantHash(self, input, method = "multiplication"):
		#convert input to int of base 35 to account for 0-9, A-Z:
		K = int(str(input), base=36)
		if method == "division":
			return self.DivisionHash(K)
		elif method == "multiplication":
			return self.MultiplicationHash(K)

	def DivisionHash(self, K):
		m = self.m
		return K % m
	
	def MultiplicationHash(self, K, A = 5**(0.5)/2 - 0.5, W = 1000):
		m = self.m
		K = K%(36**6) #cut off most significant bits
		return math.floor((m/W) * ((K*A) % W))



