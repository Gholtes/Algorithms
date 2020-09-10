class node:
    '''node for linked list type structures'''
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return str(self.val)

class stackLL:
    '''stack data structure (Last in First out) based on linked lists'''
    def __init__(self):
        self.top = None
        self.size = 0

    def add(self, val):
        newNode = node(val)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    
    def get(self):
        if self.top == None:
            return None
        else:
            topVal = self.top
            self.top = topVal.next
            self.size -= 1
            return topVal.val

class stackL:
	'''stack data structure (Last in First out) based on lists / arrays'''
	def __init__(self):
		self.items = []
	def add(self, x):
		self.items.append(x)
	def get(self):
		if len(self.items) == 0:
			return None
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def __len__(self):
		return len(self.items)
	def __repr__(self):
		return str(self.items)
