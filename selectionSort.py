def selection_sort(A):
	'''sort an array A with selection sort'''
	n = len(A)
	for k in range(n,1,-1): #as we know that the nth largest element will be in place 
							#after the nth pass through the array, so dont check it again
		max_seen = A[0]
		max_seen_i = 0

		for i in range(k):
			if A[i] > max_seen:
				max_seen_i, max_seen = i, A[i]
		
		#Swap A at kth position and max seen
		tmp = A[k-1]
		A[k-1] = max_seen
		A[max_seen_i] = tmp
	return A

