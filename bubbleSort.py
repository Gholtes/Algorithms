
def bubble_sort(A):
	'''sort an array A with bubble sort'''
	n = len(A)
	for k in range(n,1,-1): #as we know that the nth largest element will be in place 
							#after the nth pass through the array, so dont check it again
		for i in range(k-1):
			if A[i] > A[i+1]:
				tmp = A[i+1]
				A[i+1] = A[i]
				A[i] = tmp
	return A
