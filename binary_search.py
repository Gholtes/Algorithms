def bin_search_rec(arr, key, sorted = False):
	if not sorted:
		arr.sort() #sort array
	
	n = len(arr)

	if n > 0:
		if arr[n//2] == key:
			return True
		elif arr[n//2] > key:
			return bin_search_rec(arr[:n//2], key, sorted=True)
		else:
			return bin_search_rec(arr[n//2+1:], key, sorted=True)
	else:
		return False

def bin_search_iter(arr, key, sorted = False):
	if not sorted:
		arr.sort() #sort array
	
	n = len(arr)

	while n > 0:
		if arr[n//2] == key:
			return True
		elif arr[n//2] > key:
			arr = arr[:n//2]
			n = len(arr)
		else:
			arr = arr[n//2+1:]
			n = len(arr)
	
	return False

print(bin_search_rec([1,4,5,6,3,2,4,5,6,7], 2))
print(bin_search_iter([1,4,5,6,3,2,4,5,6,7], 2))