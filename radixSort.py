def radixSort(A, lengthNums, base = 10):
	for i in range(lengthNums):
		round = 10**i
		power = 10**(i+1)
		#init array
		Adigit = ["" for i in A]
		for j in range(len(A)):
			Adigit[j] = A[j] % power // round #get the int in the ith position of the number
		
		################
		###COUNT SORT###
		################
		#perform a count sort in Adigit, but transfer sort order to A as well
		L = [0 for i in range(11)]
		output = ["" for i in range(len(A))]
		outputA = ["" for i in range(len(A))]
		#count A in L
		for a in Adigit:
			L[a] += 1

		#calc cumulative sum in L, 
		for i in range(1,len(L)):
			L[i] += L[i-1]

		#use counts to position each element of A within output
		#decrement counts each time
		for pos in range(len(A)):
			outputA[L[Adigit[pos]]-1] = A[pos]
			L[Adigit[pos]] -= 1
	
		A = outputA
	
	return(A)
