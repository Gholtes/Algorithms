def merge_sort(A):
	'''perform a merge sort'''
	n = len(A)

	if n <= 1:
		
		return A #base
	
	else:
		
		left = merge_sort(A[:n//2])
		right = merge_sort(A[n//2:])
		
		l, r, i = 0, 0, 0

		while l < len(left) and r < len(right):
			if left[l] < right[r]:
				A[i] = left[l]
				l += 1
				i += 1
			else:
				A[i] = right[r]
				r += 1
				i += 1
		#use up left over elements
		while l < len(left):
			A[i] = left[l]
			l += 1
			i += 1

		while r < len(right):
			A[i] = right[r]
			r += 1
			i += 1

		return A


print(merge_sort([9,8,7,6,0,1,5]))

