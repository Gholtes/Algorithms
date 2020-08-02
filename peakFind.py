def peakFind1D(vec):
	'''
	Spec: 
	Given [a,b,c,d,e,f,g,h,i]
	Position 2 is a peak if and only if b ≥ a and b ≥ c. Position 9 is a peak if i ≥ h.
	'''

	Complete = False
	n = len(vec) - 1 
	n_half = round(n / 2)

	while not Complete:
		#start at n/2
		#end case
		if n_half == 0:
			if vec[n_half] > vec[n_half+1]:
				Complete = True
				return vec[n_half]
			else:
				return None
		elif n_half == n:
			if vec[n_half] > vec[n_half-1]:
				Complete = True
				return vec[n_half]
			else:
				return None
		#usual algo
		elif vec[n_half] > vec[n_half-1] and vec[n_half] > vec[n_half+1]:
			Complete = True
			return vec[n_half]
		elif vec[n_half] < vec[n_half+1]:
			# print("moving up")
			n_half+=1
		elif vec[n_half] < vec[n_half-1]:
			# print("moving down")
			n_half+= -1

