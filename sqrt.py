
def sqrt(a, threshold = 0.00000001, maxIter = 50):
	'''Calculate the square root of 'a' using newtons method'''
	Xi = 1.0 #a starting guess
	Delta = 1.0
	cnt = 1
	while Delta > threshold and cnt <= maxIter:
		newXi = (Xi + a / Xi) / 2
		Delta = abs(newXi - Xi)
		Xi = newXi
		cnt += 1
	return Xi

