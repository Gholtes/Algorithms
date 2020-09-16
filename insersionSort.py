def insertion_sort(A):
	for j in range(1,len(A)):
		currentVal = A[j]
		while j>0 and currentVal < A[j-1]:
			#swap down into the already sorted subarray
			A[j] = A[j-1]
			j -= 1
		A[j] = currentVal #insert current value
	return A

