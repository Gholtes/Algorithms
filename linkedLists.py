class node:
	'''node for linked list type structures'''
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None
	
	def __repr__(self):
		return str(self.val)

class singlyLinkedList(object):
	'''stack data structure (Last in First out) based on linked lists'''
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def addHead(self, val):
		newNode = node(val)

		if self.head == None and self.tail == None: #catch empty
			self.head = newNode
			self.tail = newNode
		else:
			newNode.next = self.head
			self.head = newNode
		
		self.size += 1
	
	def addTail(self, val):
		newNode = node(val)

		if self.tail == None and self.tail == None: #catch empty
			self.head = newNode
			self.tail = newNode
		else:
			newNode.next = None
			self.tail.next = newNode
			self.tail = newNode
		
		self.size += 1
	
	def delHead(self):
		if self.head == None: #catch empty
			return None
		if self.head.next == None: #last item in the list:
			node = self.head
			self.head = None
			self.tail = None
			self.size -= 1
			return node
		node = self.head
		self.head = node.next
		node.next = None #break from list
		self.size -= 1
		return node
	
	def delTail(self):
		'''In a singly linked list this is slow at O(n) as we need to traverse the whole list'''
		if self.head == None: #catch empty
			return None
		if self.head.next == None: #last item in the list:
			node = self.head
			self.head = None
			self.tail = None
			self.size -= 1
			return node
		currentTail = self.tail
		newTail = self.head
		#traverse
		while newTail.next != currentTail:
			newTail = newTail.next
		
		self.tail = newTail
		self.tail.next = None #break current tail from list
		self.size -= 1
		return currentTail

class doublyLinkedList(object):
	'''stack data structure (Last in First out) based on linked lists'''
	def __init__(self):
		#nodes
		self.headSentinal = node(None)
		self.tailSentinal = node(None)
		#vars
		self.size = 0
		#links
		self.headSentinal.next = self.tailSentinal
		self.tailSentinal.prev = self.headSentinal

	def insertNode(self, val, leadingNode, trailingNode):
		'''insert a node between two other nodes'''
		if leadingNode.next != trailingNode:
			raise IndexError("Leading and trailing nodes do not directly link")
		
		newNode = node(val)
		newNode.next = trailingNode
		newNode.prev = leadingNode
		leadingNode.next = newNode
		trailingNode.prev = newNode
		self.size += 1
		self.reassignNames()

	def delNode(self, node):
		if self.size == 0:
			return None
		node.prev.next = node.next
		node.next.prev = node.prev
		self.size -= 1
		self.reassignNames()
		return node.val

	def addHead(self, val):
		self.insertNode(val, self.headSentinal, self.headSentinal.next)
		
	def addTail(self, val):
		self.insertNode(val, self.tailSentinal.prev, self.tailSentinal)
	
	def delHead(self):
		Node = self.delNode(self.headSentinal.next)
		return Node
	
	def delTail(self):
		Node = self.delNode(self.tailSentinal.prev)
		return Node
	
	def reassignNames(self):
		if self.headSentinal.next == self.tailSentinal:
			#list is empty
			self.head = None
			self.tail = None
			self.size = 0
		else:
			self.head = self.headSentinal.next
			self.tail = self.tailSentinal.prev