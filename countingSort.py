
def countSort(A, k):
	'''sorts a list, A, which can take values between [0, k] using a counting sort'''
	#init arrays
	L = [0 for i in range(k+1)]
	output = ["" for i in range(len(A))]
	#count A in L, O(n)
	for a in A:
		L[a] += 1

	#calc cumulative sum in L, O(k)
	for i in range(1,len(L)):
		L[i] += L[i-1]

	#use counts to position each element of A within output
	#decrement counts each time
	for a in A:
		output[L[a]-1] = a
		L[a] -= 1

	return output
