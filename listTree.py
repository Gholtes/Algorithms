class listTree(object):
	'''
	use python lists to create a tree structure class
	This version assimes the tree is a binary tree, so each node is given as
	[root, [left child], [right chile]]
	no properties on keys
	'''
	def __init__(self, root = None):
		self.tree = [root, [None], [None]]

	#make new nodes
	def newNode(self, value, left=None, right=None):
		return [value, [left], [right]]
	
	# Get info on a node and navigate the tree
	def getVal(self, node):
		if len(node) == 1:
			return self.getVal(node[0])
		return node[0]
	def getLeft(self, node):
		if len(node) == 1:
			return self.getLeft(node[0])
		return node[1]
	def getRight(self, node):
		if len(node) == 1:
			return self.getRight(node[0])
		return node[2]

	#set values without checks
	def setLeft(self, node, val):
		if len(node) == 1:
			return self.setLeft(node[0], val)
		node[1][0] = val
	def setRight(self, node, val):
		if len(node) == 1:
			return self.setRight(node[0], val)
		node[2][0] = val
	
	# add nodes into the tree
	def addRightNode(self, node, newValue):
		T2 = self.getRight(node)
		if T2[0] == None: T2 = None
		self.setRight(node,
					  self.newNode(newValue, None, T2))

	def addLeftNode(self, node, newValue):
		print(node)
		T1 = self.getLeft(node)
		if T1[0] == None: T1 = None
		self.setLeft(node,
				     self.newNode(newValue, T1, None))
	
	#hidden
	def __repr__(self):
		return str(self.tree)


