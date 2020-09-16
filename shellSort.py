def shell_sort(A):
	sublist_count = len(A) // 2

	while sublist_count > 0:
		for start in range(sublist_count):

			
			gap_insertion_sort(A, start, sublist_count)
		print(sublist_count, A)
		sublist_count = sublist_count // 2
	
	return A

def gap_insertion_sort(A, start, gap):
	for i in range(start+gap, len(A), gap):
		#insersion sort
		currentVal = A[i]
		position = i

		while position >= gap and currentVal < A[position-gap]:

			#swap down into the already sorted subarray
			A[position] = A[position-gap]
			position -= gap

		A[position] = currentVal #insert current value

