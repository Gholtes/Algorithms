class heap():
	'''Properties
	Accessing elements
	Root: i = 1
	Left child of element i = 2i
	Right child of element i = 2i+1
	Parent of node i = i / 2 (need to round down)
	'''
	def __init__(self, A = None):
		if A == None:
			#make empty heap
			self.A = []
		else:
			self.A = A
			self.buildMaxHeap()

	def max_heapify(self, i):
		L = self.left(i)
		R = self.right(i)
		print("iLR",i, L,R)

		Largest = i
		
		try:
			if self.A[R] > self.A[Largest]:
				Largest  = R
		except IndexError:
			pass	

		try:
			if self.A[L] > self.A[Largest]:
				Largest = L
		except IndexError:
			pass
		
		if Largest != i:
			#swap i and Largest
			Ai = self.A[i]
			AL = self.A[Largest]
			self.A[i] = AL
			self.A[Largest] = Ai
			#continue up tree
			print(Largest, i)
			if i > 0:
				self.max_heapify(i)
		
		if i > 0:
			self.max_heapify(self.parent(i))

	def left(self, i):
		return 2*(i+1)-1
	
	def right(self, i):
		return 2*(i+1) + 1-1

	def parent(self, i):
		return (i+1) // 2 - 1

	def buildMaxHeap(self):
		iter = list(range(len(self.A)//2 +1))
		iter.reverse()
		for i in iter:
			print(i)
			self.max_heapify(i)

		print(self.A)
	
	def disp(self, i=0):
		L = self.left(i)
		R = self.right(i)

		error = ""
		try:
			AR = self.A[R] 
			if AR > self.A[i]: error = ", error"
		except IndexError:
			AR = None	

		try:
			AL = self.A[L] 
			if AL > self.A[i]: error = ", error"
		except IndexError:
			AL = None	
		

		print("i: {3} node: {0} | L: {1}, R: {2}{4}".format(self.A[i], AL, AR, i, error))
		
		if AL != None:
			self.disp(L)
		if AR != None:
			self.disp(R)


class heap2():
	'''Properties
	Accessing elements
	Root: i = 1
	Left child of element i = 2i
	Right child of element i = 2i+1
	Parent of node i = i / 2 (need to round down)
	'''
	def __init__(self, A = None):
		if A:
			self.size = len(A)
			self.A = A
			self.A.insert(0,0)
			self.build_heap()
		else:
			self.A = [0]
			self.size = 0
	
	def insert(self, x):
		self.A.append(x)
		self.size += 1
		self.min_heapify_up(self.size)

	def min_heapify_up(self, i):
		while i > 1:
			if self.A[i] < self.A[i//2]:
				#swap parent, child
				tmp = self.A[i//2]
				self.A[i//2] = self.A[i]
				self.A[i] = tmp
			i = i // 2

	def min_heapify_down(self, i):
		while i * 2 <= self.size:
			minChild = self.min_child(i)
			if self.A[i] > self.A[minChild]:
				tmp = self.A[i]
				self.A[i] = self.A[minChild]
				self.A[minChild] = tmp
			i = minChild
		
	def min_child(self, i):
		if i * 2 + 1 > self.size:
			return i * 2
		else:
			if self.A[i * 2 + 1] > self.A[i * 2]:
				return i * 2
			else:
				return i * 2 + 1
	
	def getRoot(self):
		root = self.A[1]
		self.A[1] = self.A[self.size] #set root as last item
		self.size -= 1
		self.A.pop() #remove last item
		self.min_heapify_down(1)
		return root
	
	def build_heap(self):
		middle = self.size // 2
		for i in range(middle, 0,-1):
			print(i)
			self.min_heapify_down(i)
		print(self.A)
	
	def __repr__(self):
		return str(self.A)


h = heap2([25,4,2,3,6,8,1,0,2,9,12,2])

print(h)