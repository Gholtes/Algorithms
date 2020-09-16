def quick_sort(A):
	return quick_sort_help(A, 0, len(A)-1)

def quick_sort_help(A, first, last):

	if first < last:
		
		splitpoint = partition(A, first, last)
		
		quick_sort_help(A, first, splitpoint-1)
		quick_sort_help(A, splitpoint+1, last)

		return A

def partition(A, first, last):
	pivot = A[first]
	left = first + 1
	right = last
	done = False

	while not done:
		print(left,right,A)
		#more markers
		if left <= right and A[left] <= pivot:
			left += 1
		if left <= right and A[right] >= pivot:
			right -= 1
		
		if left > right:
			done = True #markers crossed, done
		else:
			#swap left and right values
			tmp = A[right]
			A[right] = A[left]
			A[left] = tmp
	
	#swap right and pivot
	tmp = A[first]
	A[first] = A[right]
	A[right] = tmp

	return right

print(quick_sort([0,1,0,1,0,1,0]))