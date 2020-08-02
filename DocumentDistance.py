'''Document distance'''

def DocDistance(doc1, doc2):
	#1.1) Get words in doc1
	words1 = []
	word1 = ""
	for char in doc1:
		if char.isalpha():
			word1 += char
		elif not word1 == "":
			words1.append(word1)
			word1 = ""
	if not word1 == "": #final word if the final letter is alpha
		words1.append(word1)
	
	#1.2) Get words in doc2
	words2 = []
	word2 = ""
	for char in doc2:
		if char.isalpha():
			word2 += char
		elif not word2 == "":
			words2.append(word2)
			word2 = ""
	if not word2 == "": #final word if the final letter is alpha
		words2.append(word2)
	
	#2) get word counts in docs
	counts1 = {}
	for word in words1:
		try:
			counts1[word] += 1
		except KeyError:
			counts1[word] = 1

	counts2 = {}
	for word in words2:
		try:
			counts2[word] += 1
		except KeyError:
			counts2[word] = 1
	
	#3.1 Compute Doc1 dot Doc2
	count = 0
	for word in counts1.keys():
		try:
			count += counts1[word] * counts2[word]
		except KeyError:
			pass

	#3.2 compute |Doc1|*|Doc2|
	DocLensMultiplied = len(words1) * len(words2)

	return count/DocLensMultiplied
