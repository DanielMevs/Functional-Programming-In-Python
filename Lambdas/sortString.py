def sortStringArray(input):
	strArr = input.split()
	stringSort = lambda x: ord(x[0])
	return sorted(strArr, key = stringSort)
