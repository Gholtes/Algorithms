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


h = heap([1,4,2,3,6,8,1,2,2,2,2,2])

h.disp()