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

		return "Key: {0} Parent: {1} \nLeft: {2} | Right: {3}".format(self.key, parentRepr, leftRepr, rightRepr)
	
	def display(self):
		lines, *_ = self._display_aux()
		for line in lines:
			print(line)

	def _display_aux(self):
		"""Returns list of strings, width, height, and horizontal coordinate of the root."""
		# No child.
		if self.right is None and self.left is None:
			line = '%s' % self.key
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# Only left child.
		if self.right is None:
			lines, n, p, x = self.left._display_aux()
			s = '%s' % self.key
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# Only right child.
		if self.left is None:
			lines, n, p, x = self.right._display_aux()
			s = '%s' % self.key
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# Two children.
		left, n, p, x = self.left._display_aux()
		right, m, q, y = self.right._display_aux()
		s = '%s' % self.key
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2

class SplayTree():
	def __init__(self, rootKey):
		self.root = node(rootKey)
	
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
				#splay on new node
				self.splay(newNode)
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
				#splay on node
				self.splay(nodeOfInterest)
				return nodeOfInterest
			elif nodeOfInterest.key > keyToFind:
				previousNode = nodeOfInterest
				nodeOfInterest = nodeOfInterest.left
			elif nodeOfInterest.key < keyToFind:
				previousNode = nodeOfInterest
				nodeOfInterest = nodeOfInterest.right
	
	def rotateRight(self, x):
		'''rotates a BST around this node
		it can be assumed that the left child node exists'''
		#get nodes
		p = x.parent
		g = p.parent
		T2 = x.right
		
		#check if node is root
		root = False

		if g == None:
			root = True
		
		#rotate
		x.right = p
		p.parent = x
		x.parent = g
		if g != None:
			if g.right == p:
				g.right = x
			else:
				g.left = x

		p.left = T2
		if T2 != None:
			T2.parent = p

		if root:
			self.root = x

	def rotateLeft(self, x):
		'''rotates a BST left around this node
		it can be assumed that the right child node exists'''
		#check if node is root
		p = x.parent
		g = p.parent
		T2 = x.left
		
		#check if node is root
		root = False
		if g == None:
			root = True
		
		#rotate
		x.left = p
		p.parent = x
		x.parent = g
		if g != None:
			if g.right == p:
				g.right = x
			else:
				g.left = x

		p.right = T2
		if T2 != None:
			T2.parent = p

		if root:
			self.root = x

	def splay(self, x):
		'''performs a splay operation, moving the node, x, to the root position
		The splay is done in a series of steps, each particular step depends on three factors:

		Whether x is the left or right child of its parent node, p,
		whether p is the root or not, and if not
		whether p is the left or right child of its parent, g (the grandparent of x).

		Step types:

		ZIG: this step is done when p is the root. 
		1) The tree is rotated on the edge between x and p. 
		Zig steps exist to deal with the parity issue and will be done only as the last step in a splay operation

		ZIG-ZIG: this step is done when p is not the root and x and p are either both right children or are both left children.
		1) The tree is rotated on the edge joining p with its parent g, then 
		2) rotated on the edge joining x with p.

		ZIG-ZAG: this step is done when p is not the root and x is a right child and p is a left child or vice versa. 
		1) The tree is rotated on the edge between p and x, 
		2) and then rotated on the resulting edge between x and g.
		'''
		p = x.parent
		#check if x is the root already
		if p == None:
			#x is root, break
			return x
		
		#Checks
		#Whether x is the left or right child of its parent node, p,
		relationToP = "left"
		if p.right == x: relationToP= "right"

		#whether p is the root or not, and if not
		pIsRoot = False
		if p.parent == None: pIsRoot = True
		
		#whether p is the left or right child of its parent, g (the grandparent of x).
		pRelationToG = "left"
		if pIsRoot:
			pRelationToG = None
		elif p.parent.right == p: 
			pRelationToG= "right"

		#apply rules:
		if pIsRoot:
			#Zig if p is the root node
			self.ZIG(x)
		elif relationToP == pRelationToG: 
			#ZIG-ZIG if p is not the root and x and p are either both right children or are both left children.
			self.ZIGZIG(x)
		else: 
			self.ZIGZAG(x)
		
		#call splay again
		self.splay(x)

		return True
	
	def ZIG(self, x):
		'''ZIG: this step is done when p is the root. 
		1) The tree is rotated on the edge between x and p. 
		Zig steps exist to deal with the parity issue and will be done only as the last step in a splay operation'''
		p = x.parent

		#if x is the right child of p, rotate left:
		if x == p.right:
			self.rotateLeft(x)
		else: #if x is the left child of p, rotate right:
			self.rotateRight(x)
		
		return x

	def ZIGZIG(self, x):
		'''ZIG-ZAG: this step is done when p is not the root and x is a right child and p is a left child or vice versa. 
		1) The tree is rotated on the edge between p and x, 
		2) and then rotated on the resulting edge between x and g.'''
		p = x.parent
		#if x is the right child of p, rotate left:
		if x == p.right:
			self.rotateLeft(x)
			self.rotateLeft(x)
		else: #if x is the left child of p, rotate right:
			self.rotateRight(x)
			self.rotateRight(x)
	
	def ZIGZAG(self, x):
		'''ZIG-ZAG: this step is done when p is not the root and x is a right child and p is a left child or vice versa. 
		1) The tree is rotated on the edge between p and x, 
		2) and then rotated on the resulting edge between x and g.'''
		p = x.parent
		#if x is the right child of p, rotate left:
		if x == p.right:
			self.rotateLeft(x)
			self.rotateRight(x)
		else: #if x is the left child of p, rotate right:
			self.rotateRight(x)
			self.rotateLeft(x)

	def min(self):
		'''return the node with the minimum key'''
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest.left == None:
				self.splay(nodeOfInterest)
				return nodeOfInterest
			else:
				nodeOfInterest = nodeOfInterest.left

	def max(self):
		'''return the node with the maximum key'''
		nodeOfInterest = self.root
		while True:
			if nodeOfInterest.right == None:
				self.splay(nodeOfInterest)
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

	def check(self, node):
		if node.left != None:
			if node.left.key < node.key:
				self.check(node.left)
			else:
				print("FAILED", node)
		if node.right != None:
			if node.right.key > node.key:
				self.check(node.right)
			else:
				print("FAILED", node)
	