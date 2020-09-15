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

class Grant_Dict_Chain:
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

class Grant_Dict_Open_Addressing:
	def __init__(self, initialContents = None, m = 11):
		#init access table as a list
		self.m = m
		self.size = 0
		self.resize_threshold = 0.7
		self.values = [None for i in range(m)]
		self.keys = [None for i in range(m)]
		
	

	def resize(self):
		if self.size / self.m > self.resize_threshold:
			#reallocate dict
			tmp = Grant_Dict_Open_Addressing(m = self.m+2)

			for i, key in enumerate(self.keys):
				if key != None and key != "_del":
					tmp[key] = self.values[i]
			
			#reinitilize
			self.m = self.m * 2
			self.values = [None for i in range(self.m)]
			self.keys = [None for i in range(self.m)]
			self.size = 0
			#rehash items from tmp
			for i, key in enumerate(tmp.keys):
				if key != None and key != "_del":
					self.__setitem__(key, tmp.values[i])

			
			
			
	def delete(self, key, i=0):
		hashedKey = self.GrantHash(key, i)

		if self.keys[hashedKey] == None:
			raise KeyError("key: {0} not in Dict".format(key))
		elif self.keys[hashedKey] == key:
			self.keys[hashedKey] = "_del"
			self.values[hashedKey] = None
			self.size -= 1
		else:
			#try next slot
			return self.delete(key, i+1)

	def __setitem__(self, key, value):
		'''key can be a int or string, value can take any form'''
		if key == "del":
			raise NameError("_del is a protected key, please do not use")
		added = self._set_item_helper(key, value, 0)
		if added:
			self.size += 1
		self.resize()

	def _set_item_helper(self, key, value, i):
		'''returns True if a new item is created, False if the item is overwritten'''
		hashedKey = self.GrantHash(key, i)

		if self.keys[hashedKey] == None or self.keys[hashedKey] == "_del":
			self.values[hashedKey] = value
			self.keys[hashedKey] = key
			return True
		elif self.keys[hashedKey] == key:
			self.values[hashedKey] = value
			return False
		else:
			#try next slot
			return self._set_item_helper(key, value, i+1)

	def __getitem__(self, key):
		'''use special class func __getitem__ to allow for GrantDictObj[Key] syntax to search dict'''
		return self._get_item_helper(key, 0)
	
	def _get_item_helper(self, key, i):
		hashedKey = self.GrantHash(key, i)
		if self.keys[hashedKey] == None or self.keys[hashedKey] == "_del": #catch deleted case
			raise KeyError("key: {0} not in Dict".format(key))
		elif self.keys[hashedKey] == key:
			# print(self.values[hashedKey])
			return self.values[hashedKey]
		else:
			return self._get_item_helper(key, i+1)
	
	def __repr__(self):
		outstr = ""
		for i, item in enumerate(self.keys):
			if item != None and item != "_del":
				outstr += str(item) + ": " + str(self.values[i]) +", "
		return outstr

	def GrantHash(self, input, i, method = "multiplication"):
		#convert input to int of base 35 to account for 0-9, A-Z:
		K = int(str(input), base=36)
		if method == "division":
			return self.DivisionHash(K*i)
		elif method == "multiplication":
			return self.MultiplicationHash(K*i)
	
	def MultiplicationHash(self, K, A = 5**(0.5)/2 - 0.5, W = 1000):
		m = self.m
		K = K%(36**6) #cut off most significant bits
		return math.floor((m/W) * ((K*A) % W))
