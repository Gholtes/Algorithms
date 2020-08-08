class node():
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None
		self.height = 0

	def rotateRight(self):
		'''rotates a BST around this node'''
		#check if node is root
		root = False
		if self.parent == None:
			root = True
		#rotate
		leftChild = self.left
		leftChildsRightChild = leftChild.right
		parent = self.parent

		self.left = leftChildsRightChild
		leftChildsRightChild.parent = self
		
		leftChild.right = self
		self.parent = leftChild
		leftChild.parent = parent

		return root

	def rotateLeft(self):
		'''rotates a BST around this node'''
		#check if node is root
		root = False
		if self.parent == None:
			root = True
		#rotate
		rightChild = self.right
		rightChildsleftChild = rightChild.left
		parent = self.parent

		self.right = rightChildsleftChild
		rightChildsleftChild.parent = self
		
		rightChild.left = self
		self.parent = rightChild
		rightChild.parent = parent

		return root
	
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

		return "Key: {0} Parent: {1} Height: {4}\nLeft: {2} | Right: {3}".format(self.key, parentRepr, leftRepr, rightRepr, self.height)

class binarySearchTree():
	def __init__(self, rootKey, balance = False):
		self.root = node(rootKey)
		self.AVLBal = balance
	
	def insert(self, keyToInsert):
		'''Add a node to the tree and return the new node
		if the key already exists, return the existing node.
		Uses AVL balancing'''
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
					#Then we went right to get here
					previousNode.right = newNode
				#recalc heights
				self.updateHeights(newNode.parent)
				if self.AVLBal:
					#Call AVL balance
					self.balance(newNode.parent)
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
		'''return the node with the minimum key'''
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest.left == None:
				return nodeOfInterest
			else:
				nodeOfInterest = nodeOfInterest.left

	def max(self):
		'''return the node with the maximum key'''
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest.right == None:
				return nodeOfInterest
			else:
				nodeOfInterest = nodeOfInterest.right
	
	def resetRoot(self):
		'''sets self.root after rotations or other root changing transforms'''
		rootCandidate = self.root
		while True:
			if rootCandidate.parent == None:
				self.root = rootCandidate
				return self.root
			else:
				rootCandidate = rootCandidate.parent
	
	def updateHeights(self, node):
		'''adds addition to all heights up from node to root'''
		if node.left != None:
			leftChildHeight = node.left.height
		else:
			leftChildHeight = -1
		
		if node.right != None:
			rightChildHeight = node.right.height
		else:
			rightChildHeight = -1
		
		node.height = max(leftChildHeight, rightChildHeight) + 1
		#move up the tree unless we are at the root
		if not node.parent == None:
			self.updateHeights(node.parent)

	def balance(self, node):
		'''Balances a BST node, then iterates up the tree'''
		if node.right == None:
			Bal = False
		else:
			if node.right.right == None:
				rightChildHeight = -1
			else:
				rightChildHeight = node.right.right.height

			if node.right.left == None: 
				leftChildHeight = -1
			else:
				leftChildHeight = node.right.left.height

			#Balance
			if rightChildHeight - leftChildHeight >= 0:
				#check if rotations are possible:
				if node.right != None:
					if node.right.left != None:
						# print("right heavy or balanced, rotating left on:\n{0}".format(node))
						#right tree is too long, balance by rotating left'''
						if node.rotateLeft():
							self.root = node.parent
						self.updateHeights(node)
			else:
				#check if rotations are possible:
				if node.right != None:
					if node.right.left != None:
						if node.right.left.right != None:
							# print("left heavy, rotating right, lefton:\n{0}".format(node))
							#left tree is too long, balance by rotating right'''
							rightChild = node.right
							rightChild.rotateRight()
							self.updateHeights(rightChild)

							if node.rotateLeft():
								self.root = node.parent
							self.updateHeights(node)

		#move up the tree unless we are at the root
		if not node.parent == None:
			self.balance(node.parent)


