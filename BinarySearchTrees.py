class node():
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None
	
	def __repr__(self):
		if self.parent == None: 
			parentRepr = None
		else: 
			parentRepr = self.parent.key

		if self.left == None: 
			leftRepr = None
		else: 
			leftRepr = self.left.key
		
		if self.right == None: 
			rightRepr = None
		else: 
			rightRepr = self.right.key

		return "Key: {0} Parent: {1}\nLeft: {2} | Right: {3}".format(self.key, parentRepr, leftRepr, rightRepr)

class binarySearchTree():
	def __init__(self, rootKey):
		self.root = node(rootKey)
	
	def insert(self, keyToInsert):
		'''Add a node to the tree and return the new node
		if the key already exists, return the existing node'''
		previousNode = None
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest == None:
				#key is not in the tree, add it
				newNode = node(keyToInsert)
				newNode.parent = previousNode
				if previousNode.key > keyToInsert:
					#Then we went left to get here
					previousNode.left = newNode
				else:
					previousNode.right = newNode
				return newNode
			elif nodeOfInterest.key == keyToInsert:
				#key is already in the tree, break
				return nodeOfInterest
			elif nodeOfInterest.key > keyToInsert:
				previousNode = nodeOfInterest
				nodeOfInterest = nodeOfInterest.left
			elif nodeOfInterest.key < keyToInsert:
				previousNode = nodeOfInterest
				nodeOfInterest = nodeOfInterest.right
	
	def find(self, keyToFind):
		'''Attempts to find a node given a key and return the existing node, or None if the node is not found'''
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest == None:
				#key is not in the tree,
				return None
			elif nodeOfInterest.key == keyToFind:
				#key is already in the tree, return the node
				return nodeOfInterest
			elif nodeOfInterest.key > keyToFind:
				previousNode = nodeOfInterest
				nodeOfInterest = nodeOfInterest.left
			elif nodeOfInterest.key < keyToFind:
				previousNode = nodeOfInterest
				nodeOfInterest = nodeOfInterest.right

	def min(self):
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest.left == None:
				return nodeOfInterest
			else:
				nodeOfInterest = nodeOfInterest.left

	def max(self):
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest.right == None:
				return nodeOfInterest
			else:
				nodeOfInterest = nodeOfInterest.right

